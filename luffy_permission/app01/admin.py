from django.contrib import admin
from app01 import models
# Register your models here.
class Per(admin.ModelAdmin):
    list_display = ['id','url','title']

admin.site.register(models.Permission,Per)

admin.site.register(models.User)
admin.site.register(models.Role)
