# Generated by Django 4.2.1 on 2023-06-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0019_remove_newuser_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="ins",
            field=models.CharField(
                choices=[
                    ("Kompyuter savatxonligi", "Kompyuter savatxonligi"),
                    ("Frontend dasturlash", "Frontend dasturlash"),
                    ("Backend dasturlash", "Backend dasturlash"),
                    ("Grafik dizeyin", "Grafik dizeyin"),
                    ("3D_Max", "3D_Max"),
                ],
                max_length=255,
            ),
        ),
    ]