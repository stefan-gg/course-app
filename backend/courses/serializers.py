from rest_framework import serializers

from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    course_image = serializers.ImageField(use_url=False, required=True)
    author_id = serializers.CharField(source = "course.author_id", required = False)
    author_username = serializers.CharField(source = "author_id.username", read_only = True)
    class Meta:
        model = Course

        fields = [
            "name",
            "short_description",
            "description",
            "price",
            "course_image",
            "author_id",
            "author_username"
        ]

        
class UpdateCourseSerializer(serializers.ModelSerializer):
    course_image = serializers.ImageField(use_url=False, required=False)

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

    def update(self, instance, validated_data):
        # If we want to change picture we need to delete the old picture
        # so we don't fill storage with pictures we don't need anymore.
        if "course_image" in validated_data.keys():
            instance.course_image.delete()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
