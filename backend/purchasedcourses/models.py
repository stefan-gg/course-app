from django.db import models

from users.models import User
from courses.models import Course


class PurchasedCourse(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    course_id = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    purchase_date = models.DateField(auto_now_add=True)
