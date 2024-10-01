# student/urls.py
from django.urls import path
from student import views

urlpatterns = [
    path('dashboard/', views.StudentDashboardView.as_view(), name='student_dashboard'),
    path('courses/', views.courses, name='student_courses'),
    path('course-enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
    path('courses/delete/<int:enrollment_id>/', views.DeleteCourseView.as_view(), name='delete_course'),

    #tutors
    path('tutors-list/', views.tutors_list, name='tutors_list'),


    #assignment
    path('assignment-list/', views.assignment_list, name='assignment_list'),



]
