from rest_framework import serializers
from .models import Category, SubCategory, Lesson, ContactMessage,CustomWebsite


class LessonSerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source="categoryID.categoryName", read_only=True)
    SubCategoryName = serializers.CharField(source="subCategoryID.subCategoryName", read_only=True)

    class Meta:
        model = Lesson
        fields = [
            "id",
            "categoryID",
            "categoryName",
            "subCategoryID",
            "SubCategoryName",
            "lessonName",
            "lessonDescription",
            "lessonImage",
            "lessonDate",
            "lessonPdf",
        ]


class SubCategorySerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source="categoryID.categoryName", read_only=True)

    class Meta:
        model = SubCategory
        fields = [
            "id",
            "categoryID",
            "categoryName",
            "subCategoryName",
            "subCategoryImage",
            "created_at",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "categoryName",
            "categoryImage",
            "created_at",
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "full_name",
            "email",
            "subject",
            "message",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["id", "created_at", "is_read"]

class CustomWebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomWebsite
        fields = "__all__"