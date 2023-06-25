# Generated by Django 4.2.1 on 2023-06-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_remove_user_is_active_remove_user_is_staff"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="direction",
            field=models.CharField(
                choices=[
                    ("literacy", "Kompyuter savatxonligi"),
                    ("frontend", "Frontend dasturlash"),
                    ("backend", "Backend dasturlash"),
                    ("desinger", "Grafik dizeyner"),
                    ("max", "3D_Max"),
                ],
                default="literacy",
                max_length=255,
                verbose_name="Yo'nalish",
            ),
        ),
    ]
