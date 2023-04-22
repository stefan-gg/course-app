from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer

class ListCreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
