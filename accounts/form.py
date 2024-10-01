# account/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Student, Tutor


class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Student
        fields = ['date_of_birth', 'profile_image', 'phone_number', 'address', 'gender', 'age']

    def save(self, commit=True):
        # Create the User first
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        # Then create the Student instance
        student = super().save(commit=False)
        student.user = user  # Link the Student to the newly created User
        if commit:
            student.save()
        return student

class TutorRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Tutor
        fields = ['username', 'email', 'password', 'bio', 'subjects', 'date_of_birth', 'profile_image', 'phone_number', 'address', 'city', 'country', 'gender', 'age']

    def save(self, commit=True):
        # Create the User first
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        # Then create the Tutor instance
        tutor = super().save(commit=False)
        tutor.user = user
        if commit:
            tutor.save()
        return tutor