from django.contrib.auth.models import AbstractUser
from django.db import models
from teacher.models import Teacher


class NewUser(models.Model):
    name = models.CharField(max_length=255, verbose_name="I.F.O")
    ps_seria = models.CharField(max_length=11,null=True, verbose_name="Passport seria va raqam ")
    ins = models.CharField(max_length=255, verbose_name="Yo'nalishi")
    teacher = models.CharField(max_length=255, verbose_name="O'qituvchi")
    numer = models.CharField(max_length=255,verbose_name="Tel numer")
    message = models.TextField(default="Siz IT PARKga registratsiyadan utdingiz", blank=True, verbose_name="Boshqa ma'lumotlar")

    def __str__(self):
        return self.name
