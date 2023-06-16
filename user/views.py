import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from accounts.models import User

# from .emailsend import email_send


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework import status
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
def login_view(request):
    data = json.loads(request.body)
    print(data)
    email = data["email"]
    passwd = data["password"]
    obj = authenticate(email=email, password=passwd)
    if obj is not None:
        if obj.is_active:
            refresh = RefreshToken.for_user(obj)
            print(refresh, "tokens")
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "role": obj.role,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response({"status": "inactive"}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(
            {"status": "authentication error"}, status=status.HTTP_401_UNAUTHORIZED
        )
