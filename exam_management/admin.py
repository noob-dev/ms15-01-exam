from django.contrib import admin
from .models import Student, Subject, Exam, Question, Choice, Answer, Result

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['student', 'question', 'selected_choice', 'short_answer_text']

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'date', 'deadline']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'score']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
