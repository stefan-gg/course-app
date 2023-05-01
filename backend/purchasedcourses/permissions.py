from rest_framework import permissions


class PurchasedCoursePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user

        if request.method in permissions.SAFE_METHODS and not user.is_authenticated:
            return False

        if user.is_user():
            return True

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.user_id == user
