# Generated by Django 4.2.1 on 2023-06-08 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0026_remove_newuser_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="newuser",
            name="teacher",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]