from django.contrib import admin

from .models.models import CustomUser

# Register your models here.

admin.site.register(CustomUser)