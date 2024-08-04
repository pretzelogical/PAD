import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_district_attorney(url):
    base_url = 'https://www.wagonercounty.ok.gov'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the profile page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    profile_data = {
        'name': 'N/A',
        'title_held': 'District Attorney',
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
        profile_data['title_held'] = title_tag.text.strip() if title_tag else 'District Attorney'

        # Image
        img_tag = widget_item.find('img', {'class': 'field u-photo'})
        profile_data['img'] = f"{base_url}{img_tag['src']}" if img_tag else 'N/A'

    # Extract email
    email_tag = soup.find('a', href=re.compile(r'mailto:general.info@da27.org'))
    profile_data['email'] = email_tag['href'].replace('mailto:', '') if email_tag else 'N/A'

    # Extract phone number for Wagoner County
    phone_tag = soup.find('li', text=re.compile(r'Wagoner County:'))
    if phone_tag:
        profile_data['phone'] = phone_tag.text.split(':')[1].strip()

    # Remove keys with None or "N/A" values
    filtered_profile_data = {k: v for k, v in profile_data.items() if v not in (None, 'N/A')}

    return filtered_profile_data

def main():
    profile_url = "https://www.wagonercounty.ok.gov/271/District-27-District-Attorney"
    
    data = scrape_district_attorney(profile_url)
    
    if data:
        data = {
            'politician': [data],
            'organization': {
                'name': 'Wagoner County',
                'org_type': 'County Council',
                'origin': 'Wagoner, OK',
                'website': 'https://www.wagonercounty.ok.gov',
                'agenda': 'https://www.wagonercounty.ok.gov/agendacenter'
            }
        }
        with open('wagoner_district_attorney.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to wagoner_district_attorney.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
