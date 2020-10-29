from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


from .serializers import UserSerializer
from .models import User


class RegisterUserViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
