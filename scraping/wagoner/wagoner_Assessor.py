import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_assessor(url):
    base_url = 'https://www.wagonercounty.ok.gov'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the profile page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    profile_data = {
        'name': 'N/A',
        'title_held': 'Assessor',
        'phone': 'N/A',
        'email': 'N/A',
        'img': 'N/A',
        'office': 'N/A',
        'district': 'N/A'
    }

    # Extract the required information from the specific CityDirectoryLeftMargin element
    city_directory = soup.find('div', {'id': 'CityDirectoryLeftMargin'})
    if city_directory:
        # Name
        name_tag = city_directory.find('h1', {'class': 'BioName'})
        profile_data['name'] = name_tag.text.strip() if name_tag else 'N/A'

        # Phone
        phone_tag = city_directory.find('a', href=re.compile(r'tel:'))
        profile_data['phone'] = phone_tag.text.strip() if phone_tag else 'N/A'

        # Image
        img_tag = city_directory.find('img', {'class': 'imageAlignRight'})
        profile_data['img'] = f"{base_url}{img_tag['src']}" if img_tag else 'N/A'

    return profile_data

def main():
    profile_url = "https://www.wagonercounty.ok.gov/directory.aspx?eid=78"
    
    data = scrape_assessor(profile_url)
    
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
        with open('wagoner_assessor.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to wagoner_assessor.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
