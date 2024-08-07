import requests
from bs4 import BeautifulSoup
import json

def scrape_sheriff(url):
    base_url = 'https://www.wagonercountyso.org'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the profile page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    profile_data = {
        'name': 'N/A',
        'title_held': 'Sheriff',
        'phone': 'N/A',
        'email': 'N/A',
        'img': 'N/A',
        'office': 'N/A',
        'district': 'N/A'
    }

    # Extract the required information from the specific classes
    row_div = soup.find('div', {'class': 'row align-items-top'})
    if row_div:
        col_md_6_image = row_div.find('div', {'class': 'col-md-6'})
        if col_md_6_image:
            # Image
            img_tag = col_md_6_image.find('img')
            profile_data['img'] = f"{base_url}/{img_tag['src']}" if img_tag else 'N/A'
            
        col_md_6_text = row_div.find_all('div', {'class': 'col-md-6'})[1]
        if col_md_6_text:
            # Name from h1 tag
            h1_tag = col_md_6_text.find('h1', {'class': 'h3'})
            if h1_tag:
                profile_data['name'] = h1_tag.text.strip().replace('Sheriff ', '')

    # Extract phone and address
    address_div = soup.find('div', {'class': 'address col-md-4 float-end py-4'})
    if address_div:
        address_tag = address_div.find('address')
        profile_data['office'] = address_tag.text.strip() if address_tag else 'N/A'

        phone_tag = address_div.find('p')
        if phone_tag:
            profile_data['phone'] = phone_tag.text.strip().replace('Phone: ', '')

    # Remove keys with None or "N/A" values
    filtered_profile_data = {k: v for k, v in profile_data.items() if v not in (None, 'N/A')}

    return filtered_profile_data

def main():
    profile_url = "https://www.wagonercountyso.org/sheriff"
    
    data = scrape_sheriff(profile_url)
    
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
        with open('wagoner_sheriff.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to wagoner_sheriff.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
