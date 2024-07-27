import json
import re
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    return text

def parse_data(text):
    data = []

    # Join lines into a single text block
    text_block = ' '.join(text.split('\n'))

    # Debugging output
    print("Text Block:", text_block[:2000])  # Print the first 2000 characters of the text block

    # More specific regular expressions to match the patterns
    state_senator_pattern = re.compile(r"DISTRICT\s+(\d+)\s+([A-Za-z\s'-]+)\s+\((R|D)\)\s+(\d+)\s+([\d.]+)\s+([\w.-]+@[\w.-]+)")
    state_rep_pattern = re.compile(r"DISTRICT\s+(\d+)\s+([A-Za-z\s'-]+)\s+\((R|D)\)\s+(\d+)\s+([\d.]+)\s+([\w.-]+@[\w.-]+)")

    # Parse State Senators
    for match in state_senator_pattern.finditer(text_block):
        district, name, party, room, phone, email = match.groups()
        data.append({
            "type": "State Senator",
            "district": int(district),
            "name": name,
            "party": party,
            "room": room,
            "phone": phone,
            "email": email
        })

    # Parse State Representatives
    for match in state_rep_pattern.finditer(text_block):
        district, name, party, room, phone, email = match.groups()
        data.append({
            "type": "State Representative",
            "district": int(district),
            "name": name,
            "party": party,
            "room": room,
            "phone": phone,
            "email": email
        })

    # Debugging output
    print("Parsed Data:")
    print(json.dumps(data, indent=2))

    return data

def save_to_json(data, json_path):
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

pdf_path = '../data/electedofficials.pdf'
json_path = '../data/elected_officials.json'

pdf_text = extract_text_from_pdf(pdf_path)
parsed_data = parse_data(pdf_text)
save_to_json(parsed_data, json_path)

print(f"Data saved to {json_path}")
