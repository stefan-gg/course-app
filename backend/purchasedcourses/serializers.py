from rest_framework import serializers

from purchasedcourses.models import PurchasedCourse


class PurchasedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedCourse
        fields = ["user_id", "course_id", "purchase_date"]


class DetailListPurchasedCourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="course_id.name")
    course_price = serializers.CharField(source="course_id.price")

    class Meta:
        model = PurchasedCourse
        fields = ["user_id", "course_name", "course_price", "purchase_date"]
