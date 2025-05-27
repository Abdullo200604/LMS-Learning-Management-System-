from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.core.exceptions import PermissionDenied

from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer

def student_register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentSignUpForm()
    return render(request, 'users/register.html', {'form': form, 'role': 'Student'})

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher_dashboard')
    else:
        form = TeacherSignUpForm()
    return render(request, 'users/register.html', {'form': form, 'role': 'Teacher'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_teacher:
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def student_dashboard(request):
    return HttpResponse("Welcome, Student!")

@login_required
def teacher_dashboard(request):
    return HttpResponse("Welcome, Teacher!")

def teacher_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_teacher:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
