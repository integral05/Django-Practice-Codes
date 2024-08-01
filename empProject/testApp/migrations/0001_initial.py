# Generated by Django 5.0.7 on 2024-08-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id",models.BigAutoField(auto_created=True,
                primary_key=True,serialize=False,
                verbose_name="ID",),),
                ("enum", models.IntegerField()),
                ("ename", models.CharField(max_length=30)),
                ("esal", models.IntegerField()),
                ("eaddr", models.CharField(max_length=30)),
            ],
        ),
    ]
