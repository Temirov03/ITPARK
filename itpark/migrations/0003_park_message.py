# Generated by Django 4.2.1 on 2023-06-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("itpark", "0002_park_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="park",
            name="message",
            field=models.TextField(null=True),
        ),
    ]