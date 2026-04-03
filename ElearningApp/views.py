from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,generics
from .models import Category,SubCategory,Lesson
from .serializers import LessonSerializer,CategorySerializerw,SubCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializerw

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all().order_by("-id")
    serializer_class = SubCategorySerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by("-id")
    serializer_class = LessonSerializer

# GET /api/categories/<category_id>/subcategories/

# class SubCategoriesByCategory(generics.ListAPIView):
#     serializer_class = SubCategorySerializer

#     def get_queryset(self):
#         category_id = self.kwargs["category_id"] #Get Id form param
#         return SubCategory.objects.all().filter(categoryID_id = category_id).order_by("-id")
    

# #

# class LessonBySubCategory(generics.ListAPIView):
#     serializer_class = LessonSerializer

#     def get_queryset(self):
#         category_id = self.kwargs["category_id"]
#         subcategory_id = self.kwargs["subcategory_id"]

#         return Lesson.objects.all().filter(
#             categoryID_id = category_id,
#             subcategoryID_id = subcategory_id
#         ).order_by("-id")