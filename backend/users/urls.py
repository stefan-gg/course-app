from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListCreateAPIView.as_view(), name="user-list-create"),
    path('user/<int:pk>', views.UserDestroyDetailUpdateAPIView.as_view(),
          name='user-destroy-detail-update')
]