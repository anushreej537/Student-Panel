from django.db import models
from admin_panel.models import Student

class Teacher_task(models.Model):
    STATUS_CHOICES = [
        ('complete','complete'),
        ('incomplete','incomplete')
    ]
    title = models.CharField(max_length = 250)
    description = models.TextField()
    status = models.CharField(max_length = 25,choices=STATUS_CHOICES,default='incomplete')
    document = models.FileField(upload_to='documents/')
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title