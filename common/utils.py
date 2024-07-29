from .models import Politician, Organization
import json


def politician_organization_from_json(file_path: str):
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    poli = Politician.from_json(json_data, save=True)
    org = Organization.from_json(json_data, members=poli, save=True)
    return (poli, org)
