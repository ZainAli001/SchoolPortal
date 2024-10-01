# account/urls.py
from django.urls import path
from .views import (StudentLoginView, TutorLoginView, 
                    StudentSignupView, TutorSignupView,LandingView)

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),  # Landing page
    path('login/student/', StudentLoginView.as_view(), name='student_login'),
    path('signup/student/', StudentSignupView.as_view(), name='student_signup'),
    path('login/tutor/', TutorLoginView.as_view(), name='tutor_login'),
    path('signup/tutor/', TutorSignupView.as_view(), name='tutor_signup'),
    # Other URLs...
]
