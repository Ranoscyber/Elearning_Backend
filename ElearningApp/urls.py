from django.urls import path
from .views import (
    CategoryListAPIView,
    SubCategoryListAPIView,
    LessonListAPIView,
    LessonDetailAPIView,
    ContactMessageCreateAPIView,
)

urlpatterns = [
    path("api/categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("api/subcategories/", SubCategoryListAPIView.as_view(), name="subcategory-list"),
    path("api/lessons/", LessonListAPIView.as_view(), name="lesson-list"),
    path("api/lessons/<int:pk>/", LessonDetailAPIView.as_view(), name="lesson-detail"),
    path("api/contact-messages/", ContactMessageCreateAPIView.as_view(), name="contact-message-create"),
]

# /api/categories/
# /api/subcategories/?category=1
# /api/lessons/?page=1&page_size=8
# /api/lessons/2/