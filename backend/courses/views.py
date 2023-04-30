from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from courses.models import Course
from courses.serializers import CourseSerializer, UpdateCourseSerializer
from courses.mixins import CourseQuerySetMixin
from courses.permissions import CoursePermission


class ListCreateCourse(
    CoursePermission, CourseQuerySetMixin, generics.ListCreateAPIView
):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]

    def perform_create(self, serializer):
        # if serializer.validated_data["author_id"] != self.request.user:
        #     raise ValidationError(
        #         detail={"error":"Invalid value was passed for the author field"}
        #         )
        # else :
        serializer.validated_data["author_id"] = self.request.user
        return super().perform_create(serializer)


class CourseDestroyDetailUpdate(
    CoursePermission, CourseQuerySetMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = Course.objects.all()
    serializer_class = UpdateCourseSerializer
    lookup_field = "pk"
    permission_classes = [CoursePermission]

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
