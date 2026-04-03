from django.contrib import admin
from .models import Category, SubCategory, Lesson, ContactMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "categoryName", "created_at"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "subCategoryName", "categoryID", "created_at"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "lessonName", "categoryID", "subCategoryID", "lessonDate"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "subject", "is_read", "created_at"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["full_name", "email", "subject", "message"]