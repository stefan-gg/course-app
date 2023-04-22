from rest_framework import serializers

from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    
    course_image = serializers.ImageField(
            use_url=False
        )

    class Meta:
        model = Course

        fields = [
            "name",
            "short_description",
            "description",
            "price",
            "course_image",
            "author_id",
        ]