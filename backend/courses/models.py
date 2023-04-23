from django.db import models
from django.utils.translation import gettext_lazy as _
import os

from users.models import User


def upload_image_to(instance, filename):
    return str(os.path.abspath(os.getcwd())) + "\\images\\" + filename


class Course(models.Model):
    name = models.CharField(max_length=128)
    short_description = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    price = models.FloatField()
    course_image = models.ImageField(
        _("Course headline image"), upload_to=upload_image_to, max_length=256
    )
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
