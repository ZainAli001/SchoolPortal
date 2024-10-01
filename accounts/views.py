# account/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View  # Import View here
from accounts.form import StudentRegistrationForm,TutorRegistrationForm
from .models import Student,Tutor
from django.utils import timezone

class LandingView(View):
    def get(self, request):
        return render(request, 'account/landing.html')






class StudentLoginView(View):
    def get(self, request):
        return render(request, 'account/student_login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'student'):
            login(request, user)
            return redirect('student_dashboard')  # Redirect to the student dashboard
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'account/student_login.html')

class StudentSignupView(View):
    def get(self, request):
        user_form = StudentRegistrationForm()
        return render(request, 'account/student_signup.html', {
            'user_form': user_form,
        })

    def post(self, request):
        user_form = StudentRegistrationForm(request.POST, request.FILES)  # Handle file uploads
        
        if user_form.is_valid():
            # Save the form, which automatically creates both User and Student
            user_form.save()
            
            messages.success(request, 'User created successfully! Please complete your profile.')
            return redirect('student_profile', user_id=user_form.instance.user.id)

        return render(request, 'account/student_signup.html', {
            'user_form': user_form,  # Render the form in case of errors
        })
class TutorLoginView(View):
    def get(self, request):
        return render(request, 'account/tutor_login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'tutor'):
            login(request, user)
            return redirect('tutor_dashboard')  # Redirect to the tutor dashboard
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'account/tutor_login.html')

class TutorSignupView(View):
    def get(self, request):
        user_form = TutorRegistrationForm()
        return render(request, 'account/tutor_signup.html', {'user_form': user_form})

    def post(self, request):
        user_form = TutorRegistrationForm(request.POST, request.FILES)  # Handle file uploads if necessary
        
        if user_form.is_valid():
            # Save the form, which automatically creates both User and Tutor
            user_form.save()
            
            messages.success(request, 'Tutor account created successfully! Please complete your profile.')
            return redirect('tutor_profile', user_id=user_form.instance.user.id)

        return render(request, 'account/tutor_signup.html', {'user_form': user_form})