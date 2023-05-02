from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from purchasedcourses.models import PurchasedCourse


class PurchasedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedCourse
        fields = ["user_id", "course_id", "purchase_date"]

    def create(self, validated_data):
        already_purchased = PurchasedCourse.objects.filter(
            user_id = validated_data["user_id"],
            course_id = validated_data["course_id"]
            )
        # User can't buy the same course two times
        if already_purchased:
            raise ValidationError({"error":"You already own this course"})
        else:
            return super().create(validated_data)

class DetailListPurchasedCourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="course_id.name")
    course_price = serializers.CharField(source="course_id.price")

    class Meta:
        model = PurchasedCourse
        fields = ["user_id", "course_name", "course_price", "purchase_date"]
