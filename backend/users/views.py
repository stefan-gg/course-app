from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from users.models import User
from users.serializers import UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer, *args, **kwargs):
       serializer.save() 

class UserDestroyDetailUpdateAPIView(generics.DestroyAPIView, 
                                     generics.RetrieveAPIView,
                                     generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def perform_update(self, serializer, *args, **kwargs):

        # I don't like the fact that i did all this in the views file
        # but i couldn't find solution that worked the way i wanted

        password = make_password(serializer.validated_data.pop("password"))
        serializer.validated_data["password"] = password

        return super().perform_update(serializer)

    def perform_destroy(self, instance, *args, **kwargs):
        return super().perform_destroy(instance)