from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time

def fetch_sitemap(sitemap_url):
    try:
        service = Service('path/to/chromedriver')  # Update with your ChromeDriver path
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(sitemap_url)
        time.sleep(5)  # Wait for the page to load
        xml_content = driver.page_source
        driver.quit()
        return xml_content
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return None

def parse_sitemap(xml_content):
    try:
        root = ET.fromstring(xml_content)
        namespaces = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        return [element.text for element in root.findall(".//url/loc", namespaces)]
    except ET.ParseError as e:
        print(f"Error parsing sitemap XML: {e}")
        return []

def scrape_faculty_info(url):
    faculty_info = {}
    try:
        service = Service('path/to/chromedriver')  # Update with your ChromeDriver path
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
        
        faculty_info['name'] = soup.find("h1").text.strip() if soup.find("h1") else "N/A"
        faculty_info['title'] = soup.find("h4").text.strip() if soup.find("h4") else "N/A"
        faculty_info['department'] = soup.find("span", string="DEPARTMENT:").find_next("span").text.strip() if soup.find("span", string="DEPARTMENT:") else "N/A"
        
        email_tag = soup.find("a", href=True, text=lambda t: t and "@" in t)
        faculty_info['email'] = email_tag.text.strip() if email_tag else "N/A"
        
        faculty_info['office'] = soup.find("span", string="Address:").find_next("span").text.strip() if soup.find("span", string="Address:") else "N/A"
        faculty_info['education'] = [ed.text.strip() for ed in soup.select("li") if "Ph.D." in ed.text or "MS" in ed.text or "MSc" in ed.text]
        faculty_info['research_interests'] = soup.find("strong", string="Research Interests:").next_sibling.strip() if soup.find("strong", string="Research Interests:") else "N/A"
        image_tag = soup.find("img", src=True)
        faculty_info['photo_url'] = image_tag['src'] if image_tag else "No image available"
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    return faculty_info

def main():
    sitemap_url = "https://www.fccollege.edu.pk/wp-sitemap-posts-wps-team-members-1.xml"
    xml_content = fetch_sitemap(sitemap_url)
    if not xml_content:
        return
    
    faculty_urls = parse_sitemap(xml_content)
    if not faculty_urls:
        return
    
    all_faculty_info = []
    for url in faculty_urls:
        info = scrape_faculty_info(url)
        if info:
            all_faculty_info.append(info)
    
    # Output scraped data
    print("Scraped Data:", all_faculty_info)

if __name__ == "__main__":
    main()