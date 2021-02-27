from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from shop.models import User
from django.shortcuts import get_object_or_404


class UserChange(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
