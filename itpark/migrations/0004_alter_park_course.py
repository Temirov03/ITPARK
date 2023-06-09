# Generated by Django 4.2.1 on 2023-06-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("itpark", "0003_park_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="park",
            name="course",
            field=models.CharField(
                choices=[
                    ("Kompyuter savatxonligi", "Kompyuter savatxonligi"),
                    ("Frontend dasturlash", "Frontend dasturlash"),
                    ("Backend dasturlash", "Backend dasturlash"),
                    ("Grafik dizeyner", "Grafik dizeyner"),
                    ("3D_Max", "3D_Max"),
                ],
                max_length=255,
            ),
        ),
    ]
