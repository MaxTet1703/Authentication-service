from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from drf_yasg import openapi
import socket
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (CustomUserRegisterSerializer,
                          CustomUserLoginSerializer,
                          CustomUserSerializer)
from .models import CustomUser


class UserRegister(APIView):

    parser_classes = (FormParser, MultiPartParser)

    @swagger_auto_schema(
        operation_description="User register with form",
        request_body=CustomUserRegisterSerializer
    )
    def post(self, request):
        print(request.data)
        serializer = CustomUserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "user was created successfylly"},
                            status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({"error": "data are incorrect"},
                        status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    parser_classes = (FormParser, MultiPartParser)
    serializer_class = CustomUserLoginSerializer

    @swagger_auto_schema(
        operation_description="User login with form",
        request_body=CustomUserLoginSerializer
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token = RefreshToken.for_user(serializer.user)
            response = Response({
                "refresh": str(token),
                "access": str(token.access_token)
            }, status=status.HTTP_200_OK)
            return response
        return Response({"error": "Password or email are wrong"},
                        status=status.HTTP_400_BAD_REQUEST)


class UserInfo(APIView):
    
    @swagger_auto_schema()
    def get(self, request):
        print(request.get_host())
        return Response(CustomUserSerializer(
                    request.user, 
                    context={"request": request}).data,
                                status=status.HTTP_200_OK
                )
