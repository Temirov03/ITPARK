from django.db import models


# Create your models here.

class Park(models.Model):
    PARK_USER = (
        ("Kompyuter savatxonligi", "Kompyuter savatxonligi"),
        ("Frontend dasturlash", "Frontend dasturlash"),
        ("Backend dasturlash", "Backend dasturlash"),
        ("3D_Max va AuthoCAD", "3D_Max va AuthoCAD"),
        ("Grafik va Web-dizayin", "Grafik va Web-dizayin"),
        ("SMM", "SMM"),
        ("Robototexnika", "Robototexnika"),
        ("Moushn grafika", "Moushn grafika (C4D)"),
        ("Mobil dasturlash", "Mobil dasturlash"),
        ("IT English", "IT English"),
    )
    course = models.CharField(max_length=255, choices=PARK_USER)
    price = models.CharField(max_length=255, verbose_name="Narxi", null=True)
    moon = models.CharField(max_length=255,verbose_name="Kurs davomiyligi",null=True)

    def __str__(self):
        return self.course
