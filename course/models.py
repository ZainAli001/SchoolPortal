# course/models.py
from django.db import models
from accounts.models import Student

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    credit_hour = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Progress in percentage
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.name}"

class Assignment(models.Model):
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} (Course: {self.course.name})"

class Grade(models.Model):
    enrollment = models.ForeignKey(Enrollment, related_name='grades', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, related_name='grades', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"Grade: {self.score} for {self.enrollment.student.user.username} in {self.assignment.title}"
