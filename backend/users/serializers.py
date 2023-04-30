from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "user_role",
        ]
        # another way of making password read_only field
        # extra_kwargs = {
        #     'password' : {'write_only' : True}
        # }

    def create(self, validated_data):
        save_user = True
        logged_user_is_admin = validated_data.pop("logged_in_user_role") == "ADMIN"

        if validated_data["user_role"] == "ADMIN" and not logged_user_is_admin:
            save_user = False
            raise ValidationError({"error": "User role cannot be set"})
        
        if save_user:
            user = User.objects.create(
                username=validated_data["username"],
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                user_role=validated_data["user_role"],
            )

            user.set_password(validated_data["password"])

            if user.user_role == user.UserRole.ADMIN:
                user.is_staff = True
                user.is_superuser = True
        
            user.save()

            return user


class UpdateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "user_role",
        ]

    def update(self, instance, validated_data):
        user_username = None
        user_email = None

        logged_user_is_admin = validated_data.pop("logged_in_user_role") == "ADMIN"

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if "password" in validated_data.keys():
            instance.set_password(validated_data["password"])

        if "username" in validated_data.keys():
            user_username = User.objects.filter(username=validated_data["username"])

        if "email" in validated_data.keys():
            user_email = User.objects.filter(email=validated_data["email"])

        if user_username:
            raise ValidationError({"error": "Username must be unique"})

        if user_email:
            raise ValidationError({"error": "Email must be unique"})

        # only admin user can give another user ADMIN role
        if instance.user_role == instance.UserRole.ADMIN and logged_user_is_admin:
            instance.is_staff = True
            instance.is_superuser = True
        else:
            instance.is_staff = False
            instance.is_superuser = False

        instance.save()

        return instance
