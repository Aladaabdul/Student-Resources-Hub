from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_name', 'email']
    ordering = ['first_name', 'last_name']


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_code', 'department']

@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'file', 'course', 'department', 'uploaded_by', 'uploaded_at']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'resource', 'commented_by']