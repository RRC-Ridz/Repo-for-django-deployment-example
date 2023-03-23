# Generated by Django 4.1 on 2023-03-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=264)),
                ("last_name", models.CharField(max_length=264)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
