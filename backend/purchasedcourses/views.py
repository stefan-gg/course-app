from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import PurchasedCourse
from .serializers import PurchasedCourseSerializer
from .serializers import DetailListPurchasedCourseSerializer
from .permissions import PurchasedCoursePermission
from .mixins import PurchasedCourseMixin


class ListPurchasedCourses(
    PurchasedCoursePermission, PurchasedCourseMixin, generics.ListAPIView
):
    queryset = PurchasedCourse.objects.all()
    serializer_class = DetailListPurchasedCourseSerializer
    permission_classes = [IsAuthenticated, PurchasedCoursePermission]


class DetailPurchasedCourses(
    PurchasedCoursePermission, PurchasedCourseMixin, generics.RetrieveAPIView
):
    queryset = PurchasedCourse.objects.all()
    serializer_class = DetailListPurchasedCourseSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticated, PurchasedCoursePermission]


# TODO check if the course is already bought by the user.
class CreatePurchase(
    PurchasedCoursePermission, PurchasedCourseMixin, generics.CreateAPIView
):
    serializer_class = PurchasedCourseSerializer
    permission_classes = [IsAuthenticated, PurchasedCoursePermission]

    def perform_create(self, serializer):
        return super().perform_create(serializer)
