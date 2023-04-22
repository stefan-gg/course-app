from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateCourse.as_view(), name='list-create-course')
]