# courses/views.py

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Course, Lesson, Assignment, Submission
from .serializers import CourseSerializer, LessonSerializer, AssignmentSerializer, SubmissionSerializer


def index(request):
    return HttpResponse("Kurslar ro'yxati yoki bosh sahifa.")

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
