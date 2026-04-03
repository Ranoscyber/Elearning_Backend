from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    categoryName = models.CharField(max_length=200)
    categoryImage = models.ImageField(upload_to="images/Category")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryName


class SubCategory(models.Model):
    categoryID = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    subCategoryName = models.CharField(max_length=200)
    subCategoryImage = models.ImageField(upload_to="images/SubCategory")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subCategoryName


class Lesson(models.Model):
    categoryID = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    subCategoryID = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    lessonName = models.CharField(max_length=200)
    lessonDescription = RichTextUploadingField()
    lessonImage = models.ImageField(upload_to="images/Lesson")
    lessonDate = models.DateTimeField(auto_now_add=True)
    lessonPdf = models.FileField(upload_to="pdfs/lessons/", null=True, blank=True)

    def __str__(self):
        return self.lessonName


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.subject}"