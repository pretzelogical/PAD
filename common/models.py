from django.db import models

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
    origin = models.CharField(blank=True, max_length=100)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=100)
    fax = models.CharField(blank=True, max_length=100)
    image = models.ImageField(blank=True, upload_to='profile_pics/%Y/%m/%d')
    description = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Politician(Profile):
    district = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    office = models.CharField(max_length=100, blank=True)
    title_held = models.CharField(max_length=100, blank=True)


class Organization(Profile):
    """ Model for organizations.
        organization.org_type can  be one of any OrgType.
        organization.members can have one or more members.
    """
    class OrgType(models.TextChoices):
        SCHOOL_BOARD = 'SCHOOL_BOARD', 'School Board'
        PARTY = 'PARTY', 'Party'
        CITY_COUNCIL = 'CITY_COUNCIL', 'City Council'

    org_type = models.CharField(max_length=100, choices=OrgType.choices)
    members = models.ManyToManyField(
        Politician,
        related_name='organizations',
        blank=True
    )
    agenda = models.URLField(blank=True)
