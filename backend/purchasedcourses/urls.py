from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListPurchasedCourses.as_view()),
    path("<int:pk>", views.DetailPurchasedCourses.as_view()),
    path("purchase-course/", views.CreatePurchase.as_view()),
]
