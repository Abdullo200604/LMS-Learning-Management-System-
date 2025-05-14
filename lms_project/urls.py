# lms_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # users ilovasining URL-lari
    path('courses/', include('courses.urls')),  # courses ilovasining URL-lari
]
