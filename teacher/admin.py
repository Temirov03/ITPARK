from django.contrib import admin
from .models import Teacher


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id","full_name","direction","phone"
    search_fields = ["direction"]