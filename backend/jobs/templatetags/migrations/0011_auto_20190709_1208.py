# Generated by Django 2.1 on 2019-07-09 12:08

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ip_city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='ip_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='ip_country',
            field=django_countries.fields.CountryField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='ip_region',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
