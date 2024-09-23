from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exams")
    title = models.CharField(max_length=100)
    date = models.DateField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.subject.name} - {self.title}"

class Question(models.Model):
    EXAM_TYPE_CHOICES = (
        ('MCQ', 'Multiple Choice Question'),
        ('SA', 'Short Answer'),
    )

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    question_type = models.CharField(max_length=3, choices=EXAM_TYPE_CHOICES)

    def __str__(self):
        return f"{self.exam.title} - {self.text[:50]}..."

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    short_answer_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.question.exam.title}"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="results")
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.user.username} - {self.exam.title} - {self.score}%"
