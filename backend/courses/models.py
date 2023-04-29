from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
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


# we want to delete the course image
# so it doesn't takes space after object is deleted
@receiver(post_delete, sender=Course)
def delete_image_hook(sender, instance, using, **kwargs):
    instance.course_image.delete()


# In case we want to do something after course object
# is updated we can use this receiver.
# I didn't had to use it at the end but i left the code in case
# if i need it in the future, so i don't need to lookup the implementation
# @receiver(post_save, sender = Course)
# def delete_old_image_hook(sender, instance, created, **kwargs):
#     if not created:
#         course = instance
