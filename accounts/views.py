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
