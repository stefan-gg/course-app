from rest_framework import generics

from purchasedcourses.models import PurchasedCourse
from purchasedcourses.serializers import PurchasedCourseSerializer
from purchasedcourses.serializers import DetailListPurchasedCourseSerializer


class ListPurchasedCourses(generics.ListAPIView):
    queryset = PurchasedCourse.objects.all()
    serializer_class = DetailListPurchasedCourseSerializer


class DetailPurchasedCourses(generics.RetrieveAPIView):
    queryset = PurchasedCourse.objects.all()
    serializer_class = DetailListPurchasedCourseSerializer
    lookup_field = "pk"


class CreatePurchase(generics.CreateAPIView):
    serializer_class = PurchasedCourseSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
