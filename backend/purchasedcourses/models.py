from django.db import models

from users.models import User
from courses.models import Course


class PurchasedCourse(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    course_id = models.ForeignKey(Course, null=False, on_delete=models.DO_NOTHING)
    purchase_date = models.DateField(auto_now_add=True)
