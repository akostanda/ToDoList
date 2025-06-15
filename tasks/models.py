from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    POSSIBLE_STATUSES = (
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, choices=POSSIBLE_STATUSES, default='pending')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
