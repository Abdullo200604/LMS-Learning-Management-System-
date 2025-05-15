from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, AssignmentViewSet, SubmissionViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
