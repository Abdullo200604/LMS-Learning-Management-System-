from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # --- mana shu joy muhim ---
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard_teacher/', views.dashboard_teacher, name='dashboard_teacher'),
    path('dashboard_student/', views.dashboard_student, name='dashboard_student'),
    path('dashboard_zamdirektor/', views.dashboard_zamdirektor, name='dashboard_zamdirektor'),
]
