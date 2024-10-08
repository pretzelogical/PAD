# Generated by Django 5.0.7 on 2024-07-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_organization_img_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politician',
            name='party',
        ),
        migrations.AddField(
            model_name='organization',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='organization',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='politician',
            name='county',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='politician',
            name='district',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='politician',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='politician',
            name='office',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='politician',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='politician',
            name='title_held',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='origin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='politician',
            name='origin',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
