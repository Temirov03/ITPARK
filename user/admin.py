from django.contrib import admin
from .models import NewUser
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id",'name', 'teacher', 'ins', 'numer']
    search_fields = ['name']
