# Generated by Django 4.2.1 on 2023-06-20 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0031_newuser_vaqt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newuser",
            name="vaqt",
        ),
    ]
