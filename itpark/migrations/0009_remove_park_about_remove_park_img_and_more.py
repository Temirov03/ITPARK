# Generated by Django 4.2.1 on 2023-06-09 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("itpark", "0008_alter_park_course"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="park",
            name="about",
        ),
        migrations.RemoveField(
            model_name="park",
            name="img",
        ),
        migrations.RemoveField(
            model_name="park",
            name="message",
        ),
        migrations.RemoveField(
            model_name="park",
            name="popular_course",
        ),
    ]
