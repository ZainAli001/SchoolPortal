# account/admin.py
from django.contrib import admin
from .models import Student, Tutor

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone_number', 'gender', 'age', 'enrollment_date',)  # List relevant fields
    search_fields = ('user__username', 'user__email')  # Allow searching by username and email

class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'subjects', 'date_of_birth', 'phone_number', 'gender', 'age', 'city', 'country',)  # List relevant fields
    search_fields = ('user__username', 'user__email')  # Allow searching by username and email

admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)
