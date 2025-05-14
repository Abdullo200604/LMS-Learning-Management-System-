from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_teacher', 'is_student', 'is_admin')
    list_filter = ('is_teacher', 'is_student', 'is_admin')
