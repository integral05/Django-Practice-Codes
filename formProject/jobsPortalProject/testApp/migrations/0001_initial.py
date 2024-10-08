# Generated by Django 5.0.7 on 2024-08-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BloreJobs",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("eligibility", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phoneNumber", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ChennaiJobs",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("eligibility", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phoneNumber", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="HydJobs",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("eligibility", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phoneNumber", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="PuneJobs",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("eligibility", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phoneNumber", models.IntegerField()),
            ],
        ),
    ]
