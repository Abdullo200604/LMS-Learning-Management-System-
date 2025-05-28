# lms_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', lambda request: HttpResponse("<h1>Dashboard sahifasi</h1>")),
    path('', lambda request: redirect('/accounts/login/')),
    path('dashboard/', login_required(lambda request: HttpResponse("<h1>Dashboard sahifasi</h1>"))),
path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]
