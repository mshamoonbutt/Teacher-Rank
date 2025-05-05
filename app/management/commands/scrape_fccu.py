from django.core.management.base import BaseCommand
from django.db import transaction
from bs4 import BeautifulSoup
import requests
import time
from app.models import Department, Course, Teacher, CourseTeacher
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Command(BaseCommand):
    help = 'Scrapes FCCU website for departments, courses, and instructors'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force update existing records',
        )
        parser.add_argument(
            '--delay',
            type=float,
            default=2.0,
            help='Delay between requests in seconds'
        )

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        return webdriver.Chrome(options=chrome_options)

    def handle(self, *args, **options):
        self.stdout.write('Starting FCCU data scraping...')
        
        # Base URL
        base_url = 'https://www.fccollege.edu.pk'
        programs_url = f'{base_url}/academics/programs/'
        delay = options['delay']
        
        try:
            # Setup Selenium WebDriver
            driver = self.setup_driver()
            
            # Get the programs page
            self.stdout.write('Accessing programs page...')
            driver.get(programs_url)
            
            # Wait for the page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Get the page source
            page_source = driver.page_source
            
            # Save the HTML for inspection
            with open('fccu_programs.html', 'w', encoding='utf-8') as f:
                f.write(page_source)
            
            self.stdout.write(self.style.SUCCESS('Successfully saved programs page!'))
            self.stdout.write('Check fccu_programs.html for details.')
            
            # Parse with BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Print the structure of the page
            self.stdout.write('\nPrograms Page Structure:')
            for tag in soup.find_all(['div', 'section', 'nav']):
                if tag.get('class'):
                    self.stdout.write(f"Tag: {tag.name}, Classes: {tag['class']}")
                    if tag.text.strip():
                        self.stdout.write(f"Content: {tag.text.strip()[:100]}...")
                    self.stdout.write('---')
            
            # Look for program links
            self.stdout.write('\nLooking for program links...')
            program_links = []
            
            # Try different common selectors for program links
            for link in soup.find_all('a'):
                href = link.get('href', '')
                text = link.text.strip()
                if href and text and ('program' in href.lower() or 'department' in href.lower()):
                    self.stdout.write(f"Found program link: {text} -> {href}")
                    program_links.append((text, href))
            
            if not program_links:
                self.stdout.write(self.style.WARNING('Could not find program links. Please check fccu_programs.html for the actual structure.'))
                return
            
            # Visit each program page
            for program_name, program_url in program_links:
                try:
                    if not program_url.startswith('http'):
                        program_url = base_url + program_url
                    
                    self.stdout.write(f"\nAccessing program page: {program_name}")
                    driver.get(program_url)
                    
                    # Wait for the page to load
                    time.sleep(delay)
                    
                    # Get the page source
                    program_source = driver.page_source
                    
                    # Save the HTML for inspection
                    with open(f'fccu_program_{program_name.lower().replace(" ", "_")}.html', 'w', encoding='utf-8') as f:
                        f.write(program_source)
                    
                    # Parse program page
                    program_soup = BeautifulSoup(program_source, 'html.parser')
                    
                    # Try to find program details
                    self.stdout.write('Looking for program details...')
                    
                    # Try different selectors for program content
                    content_selectors = [
                        'program-content',
                        'department-content',
                        'post-content',
                        'entry-content',
                        'main-content'
                    ]
                    
                    for selector in content_selectors:
                        content = program_soup.find(['div', 'article'], {'class': selector})
                        if content:
                            self.stdout.write(f"Found content with class: {selector}")
                            self.stdout.write(f"Content preview: {content.text.strip()[:200]}...")
                            break
                    
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Error processing program {program_name}: {str(e)}'))
            
            self.stdout.write(self.style.SUCCESS('Initial structure analysis complete!'))
            self.stdout.write('Please check the saved HTML files to update the selectors based on the actual website structure.')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
        finally:
            if 'driver' in locals():
                driver.quit() 