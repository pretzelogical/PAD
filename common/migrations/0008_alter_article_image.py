# Generated by Django 5.0.7 on 2024-07-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_alter_organization_members_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_pics/%Y/%m/%d'),
        ),
    ]
