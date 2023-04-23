from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCreateCourse.as_view(), name="list-create-course"),
    path(
        "course/<int:pk>",
        views.CourseDestroyDetailUpdate.as_view(),
        name="course-destroy-detail-update",
    ),
]
