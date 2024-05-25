from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models.models import CustomUser


class CustomUserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    image = serializers.ImageField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        for field in ("email", "last_name", "first_name"
                      "password1", "password2"):
            if not data.get(field):
                raise ValidationError(f"{field} must be not empty")      
        if data["password1"] != data["password2"]:
            raise ValidationError("password1 must match with passwrd2")      
        if CustomUser.objects.filter(email=data["email"]).exists():
            raise ValidationError("User with thise email is already exist")
        return data
    
    def save(self):
        CustomUser.objects.create_user(**self.validated_data)


class CustomUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if not (data.get("email") and data.get("password")):
            raise ValidationError("email and password must be not empty")
        user = CustomUser.objects.filter(email=data["email"])
        if user.exists():
            raise ValidationError("user with this email doesnt exist")
        user = user.first()
        user = user.check_password(data["password"])
        if not user:
            raise ValidationError("Email or password are wrong")
        return data
    
    def get_user(self):
        CustomUser.objects.filter(email=self.validated_data["email"]).first()