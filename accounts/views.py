from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Mana bu yerda role tekshiruvi:
            if user.is_superuser:
                return redirect('/admin/')
            elif hasattr(user, 'role'):
                if user.role == "zamdirektor":
                    return redirect('/dashboard/')
                elif user.role == "teacher":
                    return redirect('/teacher/dashboard/')
                elif user.role == "student":
                    return redirect('/student/dashboard/')
            return redirect('/')  # fallback
        else:
            return render(request, "accounts/login.html", {"error": "Login yoki parol xato"})
    return render(request, "accounts/login.html")
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # User nomi va parol tekshiruvi
        if not username or not password:
            messages.error(request, "Login va parol to‘ldirilishi shart!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Bu login band!")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz. Endi login qilishingiz mumkin!")
            return redirect('/accounts/login/')
    return render(request, "accounts/register.html")

def dashboard_admin_view(request):
    return render(request, 'accounts/dashboard_admin.html')