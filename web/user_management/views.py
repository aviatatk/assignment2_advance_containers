from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import (
    UserProfileSerializer,
    UserRegistrationSerializer,
    ChangePasswordSerializer,
)

# Endpoint for logged-in user's profile.
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint for changing password.
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            if not user.check_password(serializer.validated_data.get("old_password")):
                return Response({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data.get("new_password"))
            user.save()
            return Response({"detail": "Password updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin endpoints:

# List all users.
class UserListAdminView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# Retrieve a specific user's details.
class UserDetailAdminView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'

# Register a new user (admin only).
class UserRegistrationAdminView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
