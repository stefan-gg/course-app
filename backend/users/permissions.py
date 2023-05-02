from rest_framework import permissions


class UserPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        method = request.method

        if method == "POST" and (user.is_anonymous or user.is_staff):
            return True

        if user.is_anonymous:
            return False

        if (user.is_author() or user.is_user()) and method != "POST":
            return True

        return user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.id == request.user.id
