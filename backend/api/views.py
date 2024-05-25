from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (CustomUserRegisterSerializer,
                          CustomUserLoginSerializer)


class UserRegister(APIView):

    @swagger_auto_schema(
        operation_description="User register with form",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, default="example@gmail.com"),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING, default="Max"),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING, default="Tet"),
                "image": openapi.Schema(type=openapi.TYPE_STRING, default=""),
                "password1": openapi.Schema(type=openapi.TYPE_STRING, default="tinotarantino777"),
                "password2": openapi.Schema(type=openapi.TYPE_STRING, default="tinotarantion777"),

            }
        )
    )
    def post(self, request):
        serializer = CustomUserRegisterSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "user was created successfylly"}, status=status.HTTP_201_CREATED)
        return Response({"error": "data are incorrect"}, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    @swagger_auto_schema(
        operation_description="User login with form",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, default="example@gmail.com"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, default="tinotarantion777"),

            }
        )
    )
    def post(self, request):
        serializer = CustomUserLoginSerializer(request.data)
        if serializer.is_valid():
            user = serializer.get_user()
            token = RefreshToken.for_user(user)
            token.payload.update({
                "user_id": user.pk,
                "user_email": user.email
            })
            return Response({
                "refreshe_token": str(token),
                "access_token": str(token.access_token)
            }, status=status.HTTP_200_OK)
        return Response({"error": "Password or email are wrong"}, status=status.HTTP_400_BAD_REQUEST)
