import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_profile(url):
    base_url = 'https://www.wagonercounty.ok.gov'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the profile page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    profile_data = {
        'name': 'N/A',
        'title_held': 'N/A',
        'phone': 'N/A',
        'email': 'N/A',
        'img': 'N/A',
        'office': 'N/A',
        'district': 'N/A'
    }

    # Extract the required information from the specific widgetItem h-card element
    widget_item = soup.find('li', {'class': 'widgetItem h-card'})
    if widget_item:
        # Name
        name_tag = widget_item.find('h4', {'class': 'widgetTitle field p-name'})
        profile_data['name'] = name_tag.text.strip() if name_tag else 'N/A'

        # Title
        title_tag = widget_item.find('div', {'class': 'field p-job-title'})
        title_held = title_tag.text.strip() if title_tag else 'N/A'
        if 'District Court Clerk' in title_held:
            title_held = 'Court Clerk'
        profile_data['title_held'] = title_held

        # Email
        email_tag = widget_item.find('div', {'class': 'field u-email'})
        if email_tag:
            email_a_tag = email_tag.find('a', href=re.compile(r'mailto:'))
            profile_data['email'] = email_a_tag['href'].replace('mailto:', '') if email_a_tag else 'N/A'

        # Image
        img_tag = widget_item.find('img', {'class': 'field u-photo'})
        profile_data['img'] = f"{base_url}{img_tag['src']}" if img_tag else 'N/A'

    # Extract phone and address from the additional h-adr elements
    h_adr = soup.find_all('div', {'class': 'field h-adr'})
    for adr in h_adr:
        if 'Physical Address' in adr.text or 'Mailing Address' in adr.text:
            address_parts = []
            for part in adr.find_all('span'):
                address_parts.append(part.text.strip())
            profile_data['office'] = ' '.join(address_parts)

    # Extract phone number
    phone_tag = soup.find('div', {'class': 'field p-tel'})
    if phone_tag:
        phone_a_tag = phone_tag.find('a', href=True)
        profile_data['phone'] = phone_a_tag.text.strip() if phone_a_tag else profile_data['phone']

    # Remove keys with None or "N/A" values
    filtered_profile_data = {k: v for k, v in profile_data.items() if v not in (None, 'N/A')}

    return filtered_profile_data

def main():
    profile_urls = [
        "https://www.wagonercounty.ok.gov/160/County-Clerk",
        "https://www.wagonercounty.ok.gov/267/Court-Clerk"
    ]
    
    politician_list = []
    for url in profile_urls:
        data = scrape_profile(url)
        if data:
            politician_list.append(data)
    
    if politician_list:
        data = {
            'politician': politician_list,
            'organization': {
                'name': 'Wagoner County',
                'org_type': 'County Council',
                'origin': 'Wagoner, OK',
                'website': 'https://www.wagonercounty.ok.gov',
                'agenda': 'https://www.wagonercounty.ok.gov/agendacenter'
            }
        }
        with open('wagoner_clerks.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to wagoner_clerks.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
