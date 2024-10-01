# student/models.py
from django.db import models
from accounts.models import Student, Tutor
from course.models import Assignment

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='submissions', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='submissions', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return f"{self.student.user.username}'s submission for {self.assignment.title}"

class Feedback(models.Model):
    submission = models.ForeignKey(Submission, related_name='feedback', on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, related_name='feedback', on_delete=models.CASCADE)
    comments = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.tutor.user.username} on {self.submission.assignment.title}"
