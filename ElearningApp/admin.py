from django.contrib import admin

from .models import Category,SubCategory,Lesson

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','categoryName','created_at']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','subCategoryName','categoryID','created_at']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id','lessonName','categoryID','subCategoryID','lessonDate']


#sonar 123456
