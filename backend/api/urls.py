from django.urls import path

from .views import UserRegister, UserLogin, TokenObtainPairView

urlpatterns = (
    path("register/", UserRegister.as_view()),
    path("login/", UserLogin.as_view()),
    path("token/refresh/", TokenObtainPairView.as_view())
)