from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .user_manager import CustomUserManager

# Create your models here.


def upload_to(instance, filename):
    return "user_profile_image/{}/{}".format(instance.pk, filename)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    image = models.ImageField(upload_to=upload_to)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ()

    objects = CustomUserManager()
    
    def __str__(self):
        if not (self.first_name and self.last_name):
            return f'{self.first_name} {self.last_name}'
        return self.email

