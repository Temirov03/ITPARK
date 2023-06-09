# Generated by Django 4.2.1 on 2023-06-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="direction",
            field=models.CharField(
                choices=[
                    ("Kompyuter savatxonligi", "Kompyuter savodxonligi"),
                    ("Frontend dasturlash", "Frontend dasturlash"),
                    ("Backend dasturlash", "Backend dasturlash"),
                    ("Grafik dizeyner", "Grafik dizeyner"),
                    ("3D_Max", "3D_Max"),
                ],
                default="Kompyuter savodxonligi",
                max_length=255,
                verbose_name="Yo'nalish",
            ),
        ),
    ]
