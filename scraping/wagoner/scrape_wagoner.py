import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_wagoner():
    base_url = 'https://www.wagonercounty.ok.gov'
    url = f'{base_url}/264/Elected-Officials'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    content_divs = soup.find_all('div', class_='widget editor pageStyles narrow')
    
    politician_list = []

    for div in content_divs:
        paragraphs = div.find_all('p')
        for p in paragraphs:
            links = p.find_all('a')
            if links:
                name = links[0].text.strip()
                
                # Debugging output to understand the structure of p.text
                print(f"Processing paragraph: {p.text}")

                # Extract position and term_expires using regex
                match = re.search(r'(.*)Term expires (.*)', p.text)
                if match:
                    position = match.group(1).strip()
                    term_expires = match.group(2).strip()
                else:
                    print("Skipping paragraph as it doesn't contain expected structure.")
                    continue

                phone_tag = p.find('a', href=re.compile(r'tel:'))
                phone = phone_tag.text.strip() if phone_tag else "N/A"
                img_tag = div.find('img')
                img = f"{base_url}{img_tag['src']}" if img_tag else "N/A"

                print(f'{name}: {position} - {term_expires} ({phone})')
                print(img)

                politician_list.append({
                    'name': name,
                    'title_held': position,
                    'term_expires': term_expires,
                    'phone': phone,
                    'img': img
                })

    return politician_list

def main():
    politician_list = scrape_wagoner()
    if politician_list:
        data = {
            'politician': politician_list,
            'organization': {
                'name': 'Wagoner County',
                'org_type': 'County Council',
                'origin': 'Wagoner, OK',
                'website': 'https://www.wagonercounty.ok.gov/',
                'agenda': 'https://www.wagonercounty.ok.gov/AgendaCenter'
            }
        }
        with open('wagoner.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to wagoner.json")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
