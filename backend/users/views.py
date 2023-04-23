from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save()


class UserDestroyDetailUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def perform_update(self, serializer, *args, **kwargs):
        return super().perform_update(serializer)

    def perform_destroy(self, instance, *args, **kwargs):
        return super().perform_destroy(instance)
