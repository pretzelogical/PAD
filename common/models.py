from django.db import models
import requests
from django.core.files.base import ContentFile


# Create your models here.


class Base(models.Model):
    """Common fields for all models."""
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(Base):
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
    views = models.BigIntegerField(default=0)

    def add_image(self, img_url):
        """
        Adds an image to a profile.
        """
        print(img_url)
        response = requests.get(img_url)
        filename = img_url.split('/')[-1]
        print(response.status_code)
        self.image.save(
            filename,
            ContentFile(response.content)
        )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Politician(Profile):
    district = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    title_held = models.CharField(max_length=100, blank=True, null=True)

    class PartyChoices(models.TextChoices):
        DEMOCRAT = 'D', 'd'
        REPUBLICAN = 'R', 'r'
        INDEPENDENT = 'I', 'i'
        OTHER = 'O', 'o'

    party = models.CharField(
        max_length=1,
        choices=PartyChoices.choices,
        default=PartyChoices.OTHER
    )

    @staticmethod
    def from_json(json_data: dict, **kwargs):
        """ Converts a json field with field politician
            and object or array of objects.
            NOTE: An image for a given politician is not saved unless save=True

            kwargs:
                save: bool
                    if True, saves the Politician objects in the database
        """
        politician_data = json_data.get('politician', None)
        if not politician_data:
            raise ValueError('Invalid json file')
        if ((type(politician_data) is not list)
                and (type(politician_data) is not dict)):
            raise ValueError('Invalid json file')
        if type(politician_data) is dict:
            politician_data = [politician_data]

        poli = []
        for p in politician_data:
            img_url = p.pop('img', None)
            converted = Politician(**p)
            if img_url and kwargs.get('save', False) is True:
                converted.add_image(img_url)
            converted.save()
            poli.append(converted)
        if kwargs.get('save', False) is True:
            Politician.objects.bulk_create(poli, ignore_conflicts=True)
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
        STATE_GOVERNMENT = 'STATE_GOVERNMENT', 'State Government'
        US_CONGRESS = 'US_CONGRESS', ' US Congress'

    org_type = models.CharField(max_length=100, choices=OrgType.choices)
    members = models.ManyToManyField(
        Politician,
        related_name='organizations',
        blank=True,
    )
    agenda = models.URLField(blank=True, null=True)

    @staticmethod
    def from_json(json_data: dict, **kwargs):
        """ Converts a json field with field organization
            and object or array of objects.
            NOTE: Images and members for a given organization are
                not saved unless save=True

            kwargs:
                save: bool
                    if True, saves the Organization objects in the database
                members: list
                    list of Politician objects to add
                    to the organizations members
        """
        organization_data = json_data.get('organization', None)
        if not organization_data:
            raise ValueError('Invalid json file')
        if ((type(organization_data) is not list)
                and (type(organization_data) is not dict)):
            raise ValueError('Invalid json file')
        if type(organization_data) is dict:
            organization_data = [organization_data]

        org = []
        for o in organization_data:
            img_url = o.pop('img', None)
            converted = Organization(**o)
            if kwargs.get('save', False) is True:
                converted.save()
                if kwargs.get('members', None):
                    converted.members.add(*kwargs.get('members'))
                if img_url:
                    converted.add_image(img_url)
                converted.save()
            org.append(converted)
        return org


class Article(Base):
    title = models.CharField(max_length=100)
    url = models.URLField()
    preview = models.TextField()
    author = models.TextField()
    image = models.ImageField(
        blank=True,
        upload_to='article_pics/%Y/%m/%d',
        null=True
    )
    related = models.ManyToManyField(
        Politician,
        related_name='articles',
        blank=True,
    )

    def __str__(self):
        return self.title
