from rest_framework import serializers
from .models import Category,SubCategory,Lesson

class LessonSerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source="categoryID.categoryName",read_only = True)
    SubCategoryName = serializers.CharField(source="subCategoryID.subCategoryName",read_only = True)
    
    class Meta:
        model = Lesson
        fields = ["id","categoryID","categoryName","subCategoryID","SubCategoryName","lessonName","lessonDescription","lessonImage","lessonDate","lessonPdf"]

class SubCategorySerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source="categoryID.categoryName",read_only = True)
    lessons = LessonSerializer(many=True,read_only=True)

    class Meta:
        model = SubCategory
        fields = [
            "id",
            "categoryID",
            "categoryName",
            "subCategoryName",
            "subCategoryImage",
            "created_at",
            "lessons"
        ]

class CategorySerializerw(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True,read_only = True)

    class Meta:
        model = Category
        fields = [
            "id",
            "categoryName",
            "categoryImage",
            "created_at",
            "subcategory"
        ]