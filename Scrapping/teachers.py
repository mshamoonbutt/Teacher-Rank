import requests
from bs4 import BeautifulSoup
import time

def fetch_sitemap(url, retries=3, delay=5):
    for attempt in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to retrieve the sitemap. Status code: {response.status_code}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
    return None

def parse_sitemap(xml_content):
    soup = BeautifulSoup(xml_content, 'lxml')
    urls = [loc.text for loc in soup.find_all('loc')]
    return urls

def scrape_staff_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    staff_info = {}

    # Debugging: Print the HTML content
    print(f"Scraping URL: {url}")
    print(soup.prettify()[:1000])  # Print the first 1000 characters of the HTML for inspection

    # Extract staff name
    name_tag = soup.find('h1', class_='entry-title')
    if not name_tag:
        name_tag = soup.find('h2', class_='entry-title')
    if not name_tag:
        name_tag = soup.find('div', class_='entry-title')
    staff_info['name'] = name_tag.text.strip() if name_tag else 'N/A'

    # Extract staff position
    position = soup.find('div', class_='staff-position').text.strip() if soup.find('div', class_='staff-position') else 'N/A'
    staff_info['position'] = position

    # Extract email
    email = soup.find('a', href=lambda href: href and "mailto:" in href).text.strip() if soup.find('a', href=lambda href: href and "mailto:" in href) else 'N/A'
    staff_info['email'] = email

    # Extract department
    department = soup.find('div', class_='staff-department').text.strip() if soup.find('div', class_='staff-department') else 'N/A'
    staff_info['department'] = department

    # Extract office number
    office_number = soup.find('div', class_='staff-office-number').text.strip() if soup.find('div', class_='staff-office-number') else 'N/A'
    staff_info['office_number'] = office_number

    # Extract extension number
    extension_number = soup.find('div', class_='staff-extension-number').text.strip() if soup.find('div', class_='staff-extension-number') else 'N/A'
    staff_info['extension_number'] = extension_number

    # Extract brief profile
    profile = soup.find('div', class_='staff-profile').text.strip() if soup.find('div', class_='staff-profile') else 'N/A'
    staff_info['profile'] = profile

    return staff_info

def main():
    sitemap_url = 'https://www.fccollege.edu.pk/wp-sitemap-posts-wps-team-members-1.xml'
    xml_content = fetch_sitemap(sitemap_url)
    if not xml_content:
        return

    urls = parse_sitemap(xml_content)
    with open('staff_info.txt', 'w', encoding='utf-8') as file:
        for url in urls:
            staff_info = scrape_staff_info(url)
            if staff_info:
                file.write(f"Staff Name: {staff_info['name']}\n")
                file.write(f"Position: {staff_info['position']}\n")
                file.write(f"Email: {staff_info['email']}\n")
                file.write(f"Department: {staff_info['department']}\n")
                file.write(f"Office Number: {staff_info['office_number']}\n")
                file.write(f"Extension Number: {staff_info['extension_number']}\n")
                file.write(f"Profile: {staff_info['profile']}\n")
                file.write('-' * 40 + '\n')

if __name__ == "__main__":
    main()