from .models import Politician, Organization
import json
import os

def politician_organization_from_json(file_path: str):
    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        poli = Politician.from_json(json_data, save=True)
        org = Organization.from_json(json_data, members=poli, save=True)
        return (poli, org)
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
        print(f"Current working directory: {os.getcwd()}")
        raise e