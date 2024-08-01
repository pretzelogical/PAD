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

    # Extract the required information
    name = soup.find('h1', {'class': 'BioName'})
    name = name.text.strip() if name else "N/A"
    
    bio_text_div = soup.find('div', {'class': 'BioText'})
    title_held = "N/A"
    if bio_text_div:
        for line in bio_text_div.stripped_strings:
            if line.startswith("Title:"):
                title_held = line.replace("Title:", "").replace("Wagoner County", "").strip()
                break
    
    phone_tag = soup.find('a', href=True, string=re.compile(r'\d{3}-\d{3}-\d{4}'))
    phone = phone_tag.text.strip() if phone_tag else "N/A"
    
    email = "N/A"
    if bio_text_div:
        for tag in bio_text_div.find_all('a'):
            if tag['href'].startswith('mailto:'):
                email = tag['href'].replace('mailto:', '')
    
    img_tag = soup.find('img', {'class': 'imageAlignRight'})
    img = f"{base_url}{img_tag['src']}" if img_tag else "N/A"
    
    district = "N/A"
    if "District" in title_held:
        district_number = title_held.split(" ")[1]
        district = f"District {district_number}"

    return {
        'name': name,
        'title_held': title_held,
        'phone': phone,
        'email': email,
        'img': img,
        'address': "N/A",
        'district': district
    }

def main():
    profile_urls = [
        "https://www.wagonercounty.ok.gov/Directory.aspx?EID=26",
        "https://www.wagonercounty.ok.gov/Directory.aspx?EID=27",
        "https://www.wagonercounty.ok.gov/Directory.aspx?EID=28"
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
        with open('wagoner_commissioners.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to wagoner_commissioners.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
