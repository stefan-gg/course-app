class PurchasedCourseMixin:
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args, **kwargs)

        if user.is_user:
            return qs.filter(user_id=user)

        return None
