import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_rogers():
    base_url = 'https://www.rogerscounty.org'
    url = f'{base_url}/238/Elected-Officials'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    politicians = soup.find_all('li', class_='widgetItem h-card')

    politician_list = []

    for politician in politicians:
        name = politician.find('h4', class_='widgetTitle field p-name').text.strip()
        position = politician.find('div', class_='field p-job-title').text.strip()
        phone_tag = politician.find('div', class_='field p-tel')
        phone = phone_tag.find('a').text.strip() if phone_tag else "N/A"
        img_tag = politician.find('img', class_='field u-photo')
        img = f"{base_url}{img_tag['src']}" if img_tag else "N/A"
        
        office_tags = politician.find_all('div', class_='field p-note')
        office = "N/A"
        district = None

        for tag in office_tags:
            text = tag.text.strip()
            if 'District' in text:
                district = re.search(r'District \d+', text)
                if district:
                    district = district.group(0)
            else:
                office = text
        
        print(f'{name}: {position} - {office} ({phone})')
        print(img)
        
        politician_list.append({
            'name': name,
            'title_held': position,
            'office': office,
            'phone': phone,
            'img': img,
            'district': district
        })

    return politician_list

def main():
    politician_list = scrape_rogers()
    if politician_list:
        data = {
            'politician': politician_list,
            'organization': {
                'name': 'Rogers County',
                'org_type': 'County Council',
                'origin': 'Claremore, OK',
                'website': 'https://www.rogerscounty.org',
                'agenda': 'https://www.rogerscounty.org/agendacenter'
            }
        }
        with open('rogers.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to rogers.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()