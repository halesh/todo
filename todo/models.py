from django.db import models

# Create your models here.

class Tasks(models.Model):

    task_name = models.CharField(max_length=200, blank=False, unique=True)
    task_desc = models.CharField(max_length=1000)
    priority = models.CharField(max_length=10, default="Normal")
    task_state = models.CharField(max_length=10, default="ToDo")
    created_on = models.DateField(auto_now_add=True)
    due_date = models.DateField()
