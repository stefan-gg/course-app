from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer

#TODO add listing -> all courses for author and add user authorization

class ListCreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CourseDestroyDetailUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
