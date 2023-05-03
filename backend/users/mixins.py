class UserMixin:
    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        qs = super().get_queryset(*args, **kwargs)

        if user.is_staff:
            return qs

        return qs.filter(id=user.id)
