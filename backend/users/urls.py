from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListCreateAPIView.as_view()),
    path('user/<int:pk>', views.UserDestroyDetailUpdateAPIView.as_view())
]