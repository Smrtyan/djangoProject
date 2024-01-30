# Generated by Django 4.2.9 on 2024-01-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("env", models.CharField(max_length=255)),
                ("envName", models.CharField(max_length=255)),
                ("enterprise", models.CharField(max_length=255)),
                ("enterpriseName", models.CharField(max_length=255)),
                ("account", models.CharField(max_length=255)),
                ("accountName", models.CharField(max_length=255)),
                ("region", models.CharField(max_length=255)),
                ("regionName", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(name="MyMember",),
    ]
