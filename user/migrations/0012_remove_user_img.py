# Generated by Django 4.2.1 on 2023-06-04 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0011_alter_user_managers_remove_user_date_joined_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="img",
        ),
    ]
