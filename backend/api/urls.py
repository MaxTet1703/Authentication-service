from django.urls import path

from .views import UserRegister, UserInfo, UserLogin
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenRefreshView)

urlpatterns = (
    path("register/", UserRegister.as_view()),
    path("login/", UserLogin.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("logout/", TokenBlacklistView.as_view()),
    path("user/info/", UserInfo.as_view())
)