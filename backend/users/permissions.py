from rest_framework import permissions


class UserPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        method = request.method
        method_is_post = request.method == "POST"
        can_create_account = user.is_anonymous or user.is_staff

        # if method == "POST" and (user.is_anonymous or user.is_staff):
        #     return True

        # if user.is_anonymous:
        #     return False

        # if (user.is_author() or user.is_user()) and method != "POST":
        #     return True

        if method_is_post and can_create_account:
            return True

        can_update_account = user.is_author() or user.is_user()

        if can_update_account and not method_is_post:
            return True

        return False if user.is_anonymous else user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.id == request.user.id
