from django.shortcuts import render, redirect
from django.contrib.auth import  logout,authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()
from .forms import CustomLoginForm
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if hasattr(user, 'role'):
                if user.role == 'admin':
                    return redirect('/accounts/dashboard_admin/')
                elif user.role == 'teacher':
                    return redirect('/accounts/dashboard_teacher/')
                elif user.role == 'student':
                    return redirect('/accounts/dashboard_student/')
                elif user.role == 'zamdirektor':
                    return redirect('/accounts/dashboard_zamdirektor/')
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # user.role borligini tekshir
            role = getattr(user, 'role', None)
            if role == 'admin':
                return redirect('/accounts/dashboard_admin/')
            elif role == 'teacher':
                return redirect('/accounts/dashboard_teacher/')
            elif role == 'student':
                return redirect('/accounts/dashboard_student/')
            elif role == 'zamdirektor':
                return redirect('/accounts/dashboard_zamdirektor/')
            else:
                # role yo‘q bo‘lsa, xato chiqarsin yoki default pagega
                return redirect('/accounts/dashboard_student/')
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

@login_required
def dashboard_admin(request):
    return render(request, 'accounts/dashboard_admin.html')

@login_required
def dashboard_teacher(request):
    return render(request, 'accounts/dashboard_teacher.html')

@login_required
def dashboard_student(request):
    return render(request, 'accounts/dashboard_student.html')

@login_required
def dashboard_zamdirektor(request):
    return render(request, 'accounts/dashboard_zamdirektor.html')
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from accounts.forms import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.core.exceptions import PermissionDenied

from rest_framework import viewsets
from accounts.models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import render

def register_view(request):
    return render(request, 'users/register.html')

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
