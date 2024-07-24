#!/usr/bin/env python3
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import json
import re


def scrape_mayes():
    with open('mayes.html', 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    politicians = soup.find_all(
        'div',
        class_='col-xs-12 card__small card__center'
    )
    politician_list = []

    def is_in_district(card_body):
        desc_str = card_body.find('div', class_='card__content').p.text
        if ', District' in desc_str:
            return int(desc_str[-1])
        return None

    for politician in politicians:
        card_body = politician.find('div', class_='card__body')
        card_footer = politician.find('div', class_='card__footer')
        name = card_body.find('span').text
        title = card_body.find('div', class_='card__content').span.text
        phone = card_footer.find('div', class_='pull-right').span.text.strip()
        office = card_footer.find('div', class_='pull-left').span.text.strip()
        img = re.search(
            r'url\(([^)]+)\)',
            card_body.find('div', class_='hidden-xs cell sidebar')['style']
        ).group(1).strip().strip("'")
        print(f'{name}: {title} - {office} ({phone})')
        print(img)
        politician_list.append({
            'name': name,
            'title_held': title,
            'office': office,
            'phone': phone,
            'img': img,
            'district': is_in_district(card_body)
        })
    with open('mayes.json', 'w') as f:
        json.dump({
            'politician': politician_list,
            'organization': {
                'name': 'Mayes County',
                'org_type': 'County Council',
                'origin': 'Pryor Creek, OK',
                'website': 'https://mayes.okcounties.org',
                'agenda': 'https://mayes.okcounties.org/meetings'
            }
        }, f)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'scrape',
        type=str,
        help='Chosen scrape operation',
        nargs='?',
        default='mayes'
    )
    args = parser.parse_args()
    match args.scrape.lower():
        case 'mayes':
            scrape_mayes()
        case _:
            scrape_mayes()
