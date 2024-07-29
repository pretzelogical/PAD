from django.contrib import admin
from .models import Politician, Organization, Article

# Register your models here.


@admin.register(Politician)
class PoliticianAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
