from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"categories",CategoryViewSet,basename="categories")
router.register(r"subcategories",SubCategoryViewSet,basename="subcategories")
router.register(r"lessons",LessonViewSet,basename="lessons")


urlpatterns = [
    path("api/",include(router.urls))

    #path("api/categories/<int:category_id/subcategories",SubCategoriesByCategory.as_view(), )
]