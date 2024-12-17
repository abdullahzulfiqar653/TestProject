from rest_framework import generics
from rest_framework.permissions import AllowAny

from apis.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
