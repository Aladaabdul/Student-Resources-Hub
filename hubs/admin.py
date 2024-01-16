from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_name', 'role']
    list_select_related = ["user"]
    ordering = ['user__first_name', 'user__last_name']


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_code', 'department']
    list_select_related = ['department']

@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'file', 'course', 'department', 'uploaded_by', 'uploaded_at']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'resource', 'commented_by', 'commented_at']