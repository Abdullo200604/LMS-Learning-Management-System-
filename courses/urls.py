
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='course_index'),  # Kurslar ro'yxati yoki bosh sahifa
]