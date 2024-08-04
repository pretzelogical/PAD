import json
from wagoner_Assessor import scrape_assessor
from wagoner_Clerk import scrape_profile as scrape_clerk
from wagoner_Commissioner import scrape_profile as scrape_commissioner
from wagoner_DistrictAttorney import scrape_district_attorney
from wagoner_sheriff import scrape_sheriff
from wagoner_Treasurer import scrape_treasurer

def main():
    combined_politicians = []

    # Scrape Assessor
    assessor_data = scrape_assessor("https://www.wagonercounty.ok.gov/directory.aspx?eid=78")
    if assessor_data:
        combined_politicians.append(assessor_data)

    # Scrape Clerk and Court Clerk
    clerk_urls = [
        "https://www.wagonercounty.ok.gov/160/County-Clerk",
        "https://www.wagonercounty.ok.gov/267/Court-Clerk"
    ]
    for url in clerk_urls:
        clerk_data = scrape_clerk(url)
        if clerk_data:
            combined_politicians.append(clerk_data)

    # Scrape Commissioners
    commissioner_urls = [
        "https://www.wagonercounty.ok.gov/Directory.aspx?EID=26",
        "https://www.wagonercounty.ok.gov/Directory.aspx?EID=27",
        "https://www.wagonercounty.ok.gov/Directory.aspx?EID=28"
    ]
    for url in commissioner_urls:
        commissioner_data = scrape_commissioner(url)
        if commissioner_data:
            combined_politicians.append(commissioner_data)

    # Scrape District Attorney
    district_attorney_data = scrape_district_attorney("https://www.wagonercounty.ok.gov/271/District-27-District-Attorney")
    if district_attorney_data:
        combined_politicians.append(district_attorney_data)

    # Scrape Sheriff
    sheriff_data = scrape_sheriff("https://www.wagonercountyso.org/sheriff")
    if sheriff_data:
        combined_politicians.append(sheriff_data)

    # Scrape Treasurer
    treasurer_data = scrape_treasurer("https://oktaxrolls.com/county/Wagoner")
    if treasurer_data:
        combined_politicians.append(treasurer_data)

    # Combine results into a single JSON file
    result = {
        'politician': combined_politicians,
        'organization': {
            'name': 'Wagoner County',
            'org_type': 'County Council',
            'origin': 'Wagoner, OK',
            'website': 'https://www.wagonercounty.ok.gov',
            'agenda': 'https://www.wagonercounty.ok.gov/agendacenter'
        }
    }

    with open('wagoner.json', 'w') as f:
        json.dump(result, f, indent=4)
    print("Data saved to wagoner.json")

if __name__ == '__main__':
    main()
