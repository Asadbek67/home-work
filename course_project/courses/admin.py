from django.contrib import admin
from .models import Course, Student, Comment


admin.site.register(Course)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'enrolled_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'comment_text', 'created_at')
