from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid


# AbstractUser is being used because it comes
# with a lot of things we need
# like hashing password and all attribute fields we need for our User model
class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    # The class defines a set of choices for user roles, including admin, author, and user.
    class UserRole(models.TextChoices):
        ADMIN = (
            "ADMIN",
            _("Admin"),
        )
        AUTHOR = (
            "AUTHOR",
            _("Author"),
        )
        USER = ("USER", _("User"))

    user_role = models.CharField(
        max_length=6, choices=UserRole.choices, default=UserRole.USER
    )
    email = models.EmailField("Email address", unique=True)
    # if we don't want username field just uncomment line of code
    # below and change REQUIRED_FIELDS and run migrations after that
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    # might delete later
    def is_user(self):
        return self.user_role == self.UserRole.USER

    def is_author(self):
        return self.user_role == self.UserRole.AUTHOR
