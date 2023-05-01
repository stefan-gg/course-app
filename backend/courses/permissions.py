from rest_framework import permissions


class CoursePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            return True

        if user.is_author() or user.is_staff:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        return obj.author_id == user and user.is_author
