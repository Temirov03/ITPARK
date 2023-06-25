# Generated by Django 4.2.1 on 2023-06-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0009_remove_user_phone_user_fax_number_user_phone_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="fax_number",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone_number",
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=13, null=True, verbose_name="Tel nomer"),
        ),
    ]
