class CourseQuerySetMixin:
    _user_field = "author_id"
    # allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self._user_field] = user.id
        qs = super().get_queryset(*args, **kwargs)

        if user.is_anonymous:
            return None

        if user.is_author:
            return qs.filter(author_id = user)

        return qs
