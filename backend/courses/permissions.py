from rest_framework import permissions


# class CourseListCreatePermission(permissions.DjangoModelPermissions):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         if request.user.is_author:
#             return True

#         return False

#     def has_object_permission(self, request, view, obj):
#         return obj.author_id == request.user

class CoursePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_anonymous:
            return False

        if request.user.is_author:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False

        return obj.author_id == request.user and request.user.is_author
