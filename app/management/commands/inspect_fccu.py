from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import json

class Command(BaseCommand):
    help = 'Inspects FCCU website structure'

    def handle(self, *args, **options):
        self.stdout.write('Inspecting FCCU website structure...')
        
        # Base URL
        base_url = 'https://www.fccu.edu.pk'
        
        try:
            # Get the main page
            response = requests.get(base_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Save the HTML structure for inspection
            with open('fccu_structure.html', 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            
            # Find all divs with classes
            divs_with_classes = soup.find_all('div', class_=True)
            
            # Create a structure map
            structure = {}
            for div in divs_with_classes:
                class_name = ' '.join(div['class'])
                if class_name not in structure:
                    structure[class_name] = {
                        'count': 0,
                        'sample_content': None
                    }
                structure[class_name]['count'] += 1
                if not structure[class_name]['sample_content']:
                    structure[class_name]['sample_content'] = div.text.strip()[:100]
            
            # Save the structure map
            with open('fccu_structure.json', 'w', encoding='utf-8') as f:
                json.dump(structure, f, indent=2)
            
            self.stdout.write(self.style.SUCCESS('Successfully saved website structure!'))
            self.stdout.write('Check fccu_structure.html and fccu_structure.json for details.')
            
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data: {str(e)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}')) 