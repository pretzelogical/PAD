# How to store and use your scraped data

## Format

The format that we will be using is a json file with a form such as this

Politician fields:

  - name
  - origin
  - website
  - email
  - phone
  - fax
  - image
  - description
  - district
  - county
  - office
  - title_held


Organization fields:

  - name
  - origin
  - website
  - email
  - phone
  - fax
  - image
  - description
  - org_type
  - agenda


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

  }
}

```

## Loading


Run `python3 manage.py shell`


```python3

>> from common.utils import politicaian_organization_from_json
>> po = politicaian_organization_from_json('file.json')
```