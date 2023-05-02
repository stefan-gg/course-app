from rest_framework import permissions


# Admin can only list all courses and delete course
# User can list all courses and get course by ID
# Authors can create, see and change their own courses
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

        if request.method in permissions.SAFE_METHODS:
            return True

        if user.is_staff and request.method == "DELETE":
            return True

        return obj.author_id == user and user.is_author()
