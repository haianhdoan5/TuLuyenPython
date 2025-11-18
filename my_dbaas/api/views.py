from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import Users


# API để tạo người dùng mới (Đăng ký)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Users
