# Generated by Django 5.0.7 on 2024-07-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='politician',
            name='img_url',
        ),
        migrations.AddField(
            model_name='organization',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='politician',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='politician',
            name='party',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
