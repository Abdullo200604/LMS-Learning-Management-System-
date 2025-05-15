from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff')  # 'role' olib tashlandi
    # list_filter = ('role',)  # agar bu ham xato bersa, commentga oling
    search_fields = ('username', 'email')
