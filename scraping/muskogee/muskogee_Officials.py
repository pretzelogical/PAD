import requests
from bs4 import BeautifulSoup
import json

def scrape_official_page(url):
    base_url = 'https://muskogee.okcounties.org'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the profile page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    profile_data = {
        'name': None,
        'title_held': None,
        'phone': None,
        'email': None,
        'img': None,
        'office': None,
        'district': None
    }

    # Extract the required information from the flip-card class
    flip_card = soup.find('div', {'class': 'flip-card__front'})
    if flip_card:
        name_tag = flip_card.find('div', {'class': 'person-name'})
        title_tag = flip_card.find('div', {'class': 'person-title'})
        img_tag = flip_card.find('img')

        profile_data['name'] = name_tag.text.strip() if name_tag else None
        profile_data['title_held'] = title_tag.text.strip() if title_tag else None
        if img_tag:
            img_src = img_tag['src']
            profile_data['img'] = f"{base_url}{img_src}" if not img_src.startswith('http') else img_src

    # Extract the contact information from all info-box divs
    contact_card = soup.find_all('div', {'class': 'info-box'})
    for card in contact_card:
        title = card.find('div', {'class': 'title-simple'}).text.strip()
        
        if title == 'Contact':
            phone_tag = card.find('a', href=True, string=lambda x: 'tel' in x)
            email_tag = card.find('a', href=True, string=lambda x: '@' in x)
            profile_data['phone'] = phone_tag.text.strip() if phone_tag else None
            profile_data['email'] = email_tag.text.strip() if email_tag else None
        
        if title == 'Address':
            address_tag = card.find('div', {'class': 'info-holder'}).find('p')
            profile_data['office'] = address_tag.text.strip() if address_tag else None

    # Remove keys with None values
    filtered_profile_data = {k: v for k, v in profile_data.items() if v is not None}

    return filtered_profile_data

def main():
    urls = [
        "https://muskogee.okcounties.org/offices/commissioner-district-1",
        "https://muskogee.okcounties.org/offices/commissioner-district-2",
        "https://muskogee.okcounties.org/offices/commissioner-district-3",
        "https://muskogee.okcounties.org/offices/county-sheriff",
        "https://muskogee.okcounties.org/offices/county-assessor",
        "https://muskogee.okcounties.org/offices/county-clerk",
        "https://muskogee.okcounties.org/offices/county-treasurer",
        "https://muskogee.okcounties.org/offices/court-clerk",
        "https://muskogee.okcounties.org/offices/district-attorney"
    ]

    all_profiles = []

    for url in urls:
        data = scrape_official_page(url)
        if data:
            all_profiles.append(data)
        else:
            print(f"No data scraped for URL: {url}")

    result = {
        'politician': all_profiles,
        'organization': {
            'name': 'Muskogee County',
            'org_type': 'County Council',
            'origin': 'Muskogee, OK',
            'website': 'https://www.muskogeeonline.org',
            'agenda': 'https://www.muskogeeonline.org/government/city_council/agendas_and_minutes.php'
        }
    }

    with open('muskogee_county.json', 'w') as f:
        json.dump(result, f, indent=4)
    print("Data saved to muskogee_county.json")

if __name__ == '__main__':
    main()
