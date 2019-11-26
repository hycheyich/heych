from django.contrib import admin
from djangoapp1 import models
# Register your models here.

admin.site.register(models.Balance)
admin.site.register(models.laboratory)
admin.site.register(models.User)