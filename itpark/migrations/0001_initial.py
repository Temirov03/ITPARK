# Generated by Django 4.2.1 on 2023-06-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Park",
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
                ("course", models.CharField(max_length=255)),
                ("about", models.TextField()),
                (
                    "popular_course",
                    models.CharField(max_length=255, verbose_name="Mashhur kurslar"),
                ),
            ],
        ),
    ]