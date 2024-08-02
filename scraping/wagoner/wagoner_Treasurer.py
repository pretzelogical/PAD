import requests
from bs4 import BeautifulSoup
import json

def scrape_treasurer(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the profile page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    profile_data = {
        'name': 'Chasity Levi',
        'title_held': 'Treasurer',
        'phone': '918-485-2149',
        'email': 'treasurer@wagonercounty.ok.gov',
        'img': 'N/A',
        'office': '307 E Cherokee, Wagoner, OK',
        'district': 'N/A'
    }

    return profile_data

def main():
    profile_url = "https://oktaxrolls.com/county/Wagoner"
    
    data = scrape_treasurer(profile_url)
    
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
        with open('wagoner_treasurer.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to wagoner_treasurer.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
