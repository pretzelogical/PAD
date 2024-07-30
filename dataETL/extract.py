import xml.etree.ElementTree as ET
import json

# Load the XML file
tree = ET.parse('../data/output_annotated.xml')
root = tree.getroot()

# Helper function to extract text within bounding boxes
def extract_text(element):
    texts = []
    for text_line in element.findall('.//LTTextLineHorizontal'):
        if text_line.text:  #checking for text to exclude nonetype
            texts.append(text_line.text.strip())
    return ' '.join(texts)

# Function to extract politician information
def extract_politicians(root):
    politicians = []
    current_politician = {}
    for element in root.findall('.//LTTextBoxHorizontal'):
        text = extract_text(element)
        print(f"Extracted Text: {text}")

        # Pattern matching based on your PDF structure
        if "Phone" in text and current_politician:
            current_politician["phone"] = text.split(":")[-1].strip()
            politicians.append(current_politician)
            print(f"Added politician: {current_politician}")
            current_politician = {}
        elif "Mail" in text:
            current_politician["office"] = text.split(":")[-1].strip()
            print(f"Found office: {current_politician['office']}")
        elif "ELECTED OFFICIALS OF" in text:
            continue  # Skip header
        else:
            name_title = text.split('(')[0].strip().rsplit(' ', 1)
            if len(name_title) == 2:
                current_politician["name"] = name_title[0]
                current_politician["title_held"] = name_title[1]
                print(f"Found name and title: {current_politician}")
            elif len(name_title) == 1 and not current_politician.get("name"):
                current_politician["name"] = name_title[0]

    return politicians

# Extract organization information (hardcoded for now, can be extracted similarly)
organization = {
    "name": "Tulsa County",
    "org_type": "County Council",
    "origin": "Tulsa, OK",
    "website": "https://example.com",  # Placeholder
    "agenda": "https://example.com/meetings"  # Placeholder
}

# Extract politicians data
politicians = extract_politicians(root)
print(f"Extracted Politicians: {json.dumps(politicians, indent=2)}")

# Structure the JSON data
data = {
    "politician": politicians,
    "organization": organization
}

# Write to a JSON file
with open('../data/tulsa_elected_officials.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data extraction and JSON file creation complete.")
