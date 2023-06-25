from django.db import models


# Create your models here.

class Teacher(models.Model):
    TEACHER_USER = (
        ("Kompyuter savatxonligi o'qituvchisi", "Kompyuter savatxonligi o'qituvchisi"),
        ("Frontend dasturchi", "Frontend dasturchi"),
        ("Backend dasturchi", "Backend dasturchi"),
        ("3D_Max va AuthoCAD mutaxasisi", "3D_Max va AuthoCAD mutaxasisi"),
        ("Grafik va Web-dizayin", "Grafik va Web-dizayin"),
        ("SMM mutaxasisi", "SMM mutaxasisi"),
        ("Robototexnika mutaxasisi", "Robototexnika mutaxasisi"),
        ("Moushn grafika (C4D) mutaxasisi", "Moushn grafika (C4D) mutaxasisi"),
        ("Mobil dasturchi", "Mobil dasturchi"),
        ("IT English o'qituvchisi", "IT English o'qituvchisi"),
    )

    full_name = models.CharField(verbose_name="Ism va Familiya",null=True, max_length=255, help_text="O'qituvchini "
                                                                                                     "Ism va "
                                                                                                     "Familiyasi")
    direction = models.CharField(max_length=255, choices=TEACHER_USER, default="Kompyuter savodxonligi", verbose_name="Yo'nalish")
    phone = models.CharField(max_length=13, verbose_name="Tel nomer", null=True)
    experience = models.CharField(max_length=25, verbose_name="Tajribasi")
    imga = models.ImageField(verbose_name="O'qituvchini rasmi",upload_to='teacher_img')
    tg_user = models.CharField(max_length=255,null=True, default="https://t.me/itparksamarkand")
    github = models.CharField(max_length=255, null=True)
    instagram = models.CharField(max_length=255,null=True,default="https://instagram.com/mrit.uz?igshid"
                                                                  "=MzRlODBiNWFlZA==")
    about = models.TextField()


    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
