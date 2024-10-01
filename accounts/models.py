# account/models.py
from django.db import models
from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     date_of_birth = models.DateField(null=True, blank=True)  # DOB field
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Profile image field
#     phone_number = models.CharField(max_length=15, blank=True, null=True)  # Phone number field
#     address = models.TextField(blank=True, null=True)  # Address field
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True) 
#     age = models.IntegerField()

#     def __str__(self):
#         return self.user.username

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Directly reference User
    enrollment_date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)  # DOB field
    profile_image = models.ImageField(upload_to='student_images/', blank=True, null=True)  # Profile image field
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Phone number field
    address = models.TextField(blank=True, null=True)  # Address field
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True) 
    age = models.IntegerField(blank = True , null=True)

    def __str__(self):
        return self.user.username

class Tutor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Directly reference User
    bio = models.TextField(blank=True)
    subjects = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)  # DOB field
    profile_image = models.ImageField(upload_to='tutor_images/', blank=True, null=True)  # Profile image field
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Phone number field
    address = models.TextField(blank=True, null=True)  # Address field
    city = models.CharField(max_length=100, blank=True, null=True)  # City field
    country = models.CharField(max_length=100, blank=True, null=True)  # Country field
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True) 
    age = models.IntegerField(blank = True , null=True)

    def __str__(self):
        return self.user.username
