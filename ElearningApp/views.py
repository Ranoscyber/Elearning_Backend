from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Category, SubCategory, Lesson, ContactMessage
from .serializers import (
    CategorySerializer,
    SubCategorySerializer,
    LessonSerializer,
    ContactMessageSerializer,
)


class LessonPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"
    max_page_size = 20


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializer


class SubCategoryListAPIView(generics.ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = SubCategory.objects.select_related("categoryID").all().order_by("-id")
        category_id = self.request.query_params.get("category")

        if category_id:
            queryset = queryset.filter(categoryID_id=category_id)

        return queryset


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = LessonPagination

    def get_queryset(self):
        queryset = Lesson.objects.select_related("categoryID", "subCategoryID").all().order_by("-id")

        category_id = self.request.query_params.get("category")
        subcategory_id = self.request.query_params.get("subcategory")

        if category_id:
            queryset = queryset.filter(categoryID_id=category_id)

        if subcategory_id:
            queryset = queryset.filter(subCategoryID_id=subcategory_id)

        return queryset


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.select_related("categoryID", "subCategoryID").all()
    serializer_class = LessonSerializer


class ContactMessageCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer