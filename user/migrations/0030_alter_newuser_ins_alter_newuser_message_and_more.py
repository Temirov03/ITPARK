# Generated by Django 4.2.1 on 2023-06-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0029_alter_newuser_ps_seria"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="ins",
            field=models.CharField(max_length=255, verbose_name="Yo'nalishi"),
        ),
        migrations.AlterField(
            model_name="newuser",
            name="message",
            field=models.TextField(
                blank=True,
                default="Siz IT PARKga registratsiyadan utdingiz",
                verbose_name="Boshqa ma'lumotlar",
            ),
        ),
        migrations.AlterField(
            model_name="newuser",
            name="name",
            field=models.CharField(max_length=255, verbose_name="I.F.O"),
        ),
        migrations.AlterField(
            model_name="newuser",
            name="numer",
            field=models.CharField(max_length=255, verbose_name="Tel numer"),
        ),
        migrations.AlterField(
            model_name="newuser",
            name="ps_seria",
            field=models.CharField(
                max_length=11, null=True, verbose_name="Passport seria va raqam "
            ),
        ),
        migrations.AlterField(
            model_name="newuser",
            name="teacher",
            field=models.CharField(max_length=255, verbose_name="O'qituvchi"),
        ),
    ]
