# student/views.py
from django.views import View
from django.shortcuts import render, redirect
from course.models import Enrollment, Course,Assignment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Tutor

class StudentDashboardView(View):
    def get(self, request):
        return render(request, 'student/dashboard.html')  # Adjust the template name as needed

def courses(request):
    student = request.user.student
    enrolled_courses = Enrollment.objects.filter(student=student).select_related('course')
    return render(request, 'student/courses.html', {
        'enrolled_courses': enrolled_courses
    })

class DeleteCourseView(View):
    def post(self, request, enrollment_id):
        print(enrollment_id)
        enrollment = get_object_or_404(Enrollment, id=enrollment_id)
        enrollment.delete()
        return JsonResponse({'success': True})  # Respond with a success message
class CourseEnrollView(View):
    def get(self, request):
        courses = Course.objects.all()  # Fetch available courses
        return render(request, 'student/course_enroll.html', {'courses': courses})

    def post(self, request):
        selected_course_id = request.POST.get('course_id')
        if selected_course_id:
            # Check if the student is already enrolled in this course
            if Enrollment.objects.filter(student=request.user.student, course_id=selected_course_id).exists():
                messages.error(request, "You are already enrolled in this course.")
                return redirect('course_enroll') 
            else:
                # Enroll the student in the course
                Enrollment.objects.create(student=request.user.student, course_id=selected_course_id)
                messages.success(request, "You have successfully enrolled in the course.")

        return redirect('student_courses')  # Redirect to the course listing or dashboard
    

def tutors_list(request):
    tutors = Tutor.objects.all()  # Fetch all tutors from the database
    return render(request, 'student/tutors_list.html', {'tutors': tutors})

def assignment_list(request):
    assignment = Assignment.objects.all()  # Fetch all tutors from the database
    return render(request, 'student/assignment_list.html', {'assignment': assignment})