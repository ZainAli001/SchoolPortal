from django.contrib import admin
from .models import Course, Enrollment, Assignment, Grade

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'credit_hour')
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'progress')
    search_fields = ('student__user__username', 'course__name')
    list_filter = ('enrollment_date', 'progress')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date')
    search_fields = ('title', 'course__name')
    list_filter = ('due_date',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'assignment', 'score')
    search_fields = ('enrollment__student__user__username', 'assignment__title')
    list_filter = ('score',)
