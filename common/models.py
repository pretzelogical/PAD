from django.db import models
import json


# Create your models here.


class Common(models.Model):
    """Common fields for all models."""
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(Common):
    """ Common fields for all profiles. """
    name = models.CharField(max_length=100)
    origin = models.CharField(blank=True, max_length=100, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=100, null=True)
    fax = models.CharField(blank=True, max_length=100)
    image = models.ImageField(
        blank=True,
        upload_to='profile_pics/%Y/%m/%d',
        null=True
    )
    description = models.CharField(blank=True, max_length=500, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Politician(Profile):
    district = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    title_held = models.CharField(max_length=100, blank=True, null=True)

    def from_json(file_path: str, **kwargs):
        """ Converts a json field with field politician
            and object or array of objects
        """
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        politician_data = json_data.get('politician', None)
        if not politician_data:
            raise ValueError('Invalid json file')
        if type(politician_data) is dict:
            poli = Politician(**politician_data)
            poli = [poli]
        elif type(politician_data) is list:
            poli = [Politician(**data) for data in politician_data]
        else:
            raise ValueError('Invalid json file')
        if kwargs.get('save', False) is True:
            for p in poli:
                p.save()
        return poli


class Organization(Profile):
    """ Model for organizations.
        organization.org_type can  be one of any OrgType.
        organization.members can have one or more members.
    """
    class OrgType(models.TextChoices):
        SCHOOL_BOARD = 'SCHOOL_BOARD', 'School Board'
        PARTY = 'PARTY', 'Party'
        CITY_COUNCIL = 'CITY_COUNCIL', 'City Council',
        COUNTY_COUNCIL = 'COUNTY_COUNCIL', 'County Council'

    org_type = models.CharField(max_length=100, choices=OrgType.choices)
    members = models.ManyToManyField(
        Politician,
        related_name='organizations',
        blank=True,
        null=True
    )
    agenda = models.URLField(blank=True, null=True)
