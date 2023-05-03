from rest_framework import permissions


# Admin can only list all courses and delete course
# User can list all courses and get course by ID
# Authors can create, see and change their own courses
class CoursePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        method_is_safe = request.method in permissions.SAFE_METHODS
        user_is_author_or_admin = user.is_author() or user.is_staff

        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # if user.is_author() or user.is_staff:
        #     return True

        if method_is_safe or user_is_author_or_admin:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        method_is_safe = request.method in permissions.SAFE_METHODS
        admin_wants_to_delete = user.is_staff and request.method == "DELETE"

        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # if user.is_staff and request.method == "DELETE":
        #     return True

        if method_is_safe or admin_wants_to_delete:
            return True

        return obj.author_id == user  # and user.is_author()
