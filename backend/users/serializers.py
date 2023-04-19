from rest_framework import serializers

from .models import User

class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'role',
        ]

    def create(self, validated_data):

        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            role = validated_data['role']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    