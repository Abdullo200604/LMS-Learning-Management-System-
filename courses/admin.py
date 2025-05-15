from django.contrib import admin
from .models import Course, Lesson, Assignment, Submission

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'teacher')
    search_fields = ('title',)
    list_filter = ('teacher',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course',)
    search_fields = ('title',)
    list_filter = ('course',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lesson', 'due_date')
    list_filter = ('lesson',)
    search_fields = ('title',)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'assignment', 'student', 'submitted_at', 'grade')
    list_filter = ('submitted_at',)
    search_fields = ('student__username',)
