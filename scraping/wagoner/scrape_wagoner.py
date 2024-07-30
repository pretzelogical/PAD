import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_wagoner():
    base_url = 'https://www.wagonercounty.ok.gov/'
    url = f'{base_url}/238/Elected-Officials'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    politicians = soup.find_all('li', class_='widgetItem h-card')

    politician_list = []
    