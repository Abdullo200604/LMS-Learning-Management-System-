from django.db import models
from accounts.models import CustomUser

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='assignments/')
    student = models.ForeignKey(CustomUser, related_name='assignments', on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    teacher = models.ForeignKey(CustomUser, related_name='given_assignments', on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    deadline = models.DateTimeField()
    changed_at = models.DateTimeField(auto_now=True)  # deadline o‘zgarganda avtomatik yoziladi
    attempt = models.PositiveIntegerField(default=1)  # 3 martagacha upload huquqi
    grade = models.CharField(max_length=20, blank=True, null=True)  # Baholash uchun
    comment = models.TextField(blank=True, null=True)  # O‘qituvchi sharhi

    def __str__(self):
        return f"{self.title} - {self.student.username}"

    class Meta:
        ordering = ['-deadline']
