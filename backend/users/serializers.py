from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'user_role',
        ]
        # another way of making password read_only field
        # extra_kwargs = {
        #     'password' : {'write_only' : True}
        # }

    def create(self, validated_data):

        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            user_role = validated_data['user_role']
        )

        user.set_password(validated_data['password'])
        
        if user.user_role == user.UserRole.ADMIN:
            user.is_staff = True
            user.is_superuser = True

        print(user.user_role == user.UserRole.ADMIN)

        user.save()
        
        return user