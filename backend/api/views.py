from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (CustomUserRegisterSerializer,
                          CustomUserLoginSerializer)


class UserRegister(APIView):

    parser_classes = (FormParser, MultiPartParser)

    @swagger_auto_schema(
        operation_description="User register with form",
        request_body=CustomUserRegisterSerializer
    )
    def post(self, request):
        serializer = CustomUserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "user was created successfylly"}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({"error": "data are incorrect"}, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(TokenObtainPairView):

    parser_classes = (FormParser,)
    serializer_class = CustomUserLoginSerializer

    @swagger_auto_schema(
        operation_description="User login with form",
        request_body=CustomUserLoginSerializer
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            token = RefreshToken.for_user(serializer.user)
            return Response({
                "refreshe_token": str(token),
                "access_token": str(token.access_token)
            }, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({"error": "Password or email are wrong"}, status=status.HTTP_400_BAD_REQUEST)
