from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.mixins import UserMixin
from users.models import User
from users.permissions import UserPermission
from users.serializers import UserSerializer, UpdateUserSerializer


class UserListCreateAPIView(UserMixin, UserPermission, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    def perform_create(self, serializer, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous:
            serializer.validated_data["logged_in_user_role"] = "Anonymous"
        else:
            serializer.validated_data["logged_in_user_role"] = user.user_role
        serializer.save()


class UserDestroyDetailUpdateAPIView(
    UserMixin, UserPermission, generics.RetrieveUpdateDestroyAPIView
):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticated, UserPermission]

    def perform_update(self, serializer, *args, **kwargs):
        user = self.request.user
        serializer.validated_data["logged_in_user_role"] = user.user_role
        return super().perform_update(serializer)

    def perform_destroy(self, instance, *args, **kwargs):
        return super().perform_destroy(instance)
