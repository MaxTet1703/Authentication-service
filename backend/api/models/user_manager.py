from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email must be not empty")
        elif not password:
            raise ValueError("password must be not empty")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):

        for field in ("is_superuser", "is_active", "is_staff"):
            extra_fields.setdefault(field, True)
            if not extra_fields.get(field):
                raise ValueError(f"{field} field must be have True value")
    
        return self.create_user(email=email, password=password, **extra_fields)
