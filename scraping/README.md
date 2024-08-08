
# How to Store and Use Your Scraped Data

## Format

The format that we will be using is a JSON file with the following structure:

### Politician Fields:

- **name**: The name of the politician.
- **origin**: The origin of the politician.
- **website**: The website of the politician.
- **email**: The email address of the politician.
- **phone**: The phone number of the politician.
- **fax**: The fax number of the politician.
- **image**: The image URL of the politician.
- **description**: A description of the politician.
- **district**: The district of the politician.
- **county**: The county of the politician.
- **office**: The office of the politician.
- **title_held**: The title held by the politician.

### Organization Fields:

- **name**: The name of the organization.
- **origin**: The origin of the organization.
- **website**: The website of the organization.
- **email**: The email address of the organization.
- **phone**: The phone number of the organization.
- **fax**: The fax number of the organization.
- **image**: The image URL of the organization.
- **description**: A description of the organization.
- **org_type**: The type of the organization.
- **agenda**: The agenda of the organization.

```json
{
  "politician": [
    {
      "name": "Test name",
      "website": "website.com",
      ...
    },
    ...
  ],
  "organization": {
    "name": "Alva Martin",
    ...
  }
}
```

## Loading Data

To load your scraped data into the system, follow these steps:

1. Run the Django shell:

   ```shell
   python3 manage.py shell
   ```

2. Use the following Python code to load the data:

   ```python
   from common.utils import politician_organization_from_json
   po = politician_organization_from_json('file.json')
   ```
