from django.contrib import admin
from .models import Politician, Organization

# Register your models here.


@admin.register(Politician)
class PoliticianAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']
