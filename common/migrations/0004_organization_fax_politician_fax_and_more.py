# Generated by Django 5.0.7 on 2024-07-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_politician_party_organization_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='fax',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='politician',
            name='fax',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='organizations', to='common.politician'),
        ),
        migrations.AlterField(
            model_name='politician',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
