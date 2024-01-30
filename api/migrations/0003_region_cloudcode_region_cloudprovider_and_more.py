# Generated by Django 4.2.9 on 2024-01-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_region_delete_mymember"),
    ]

    operations = [
        migrations.AddField(
            model_name="region",
            name="cloudCode",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="region",
            name="cloudProvider",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="region",
            name="projectId",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
