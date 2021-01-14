from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum
from datetime import datetime, date
from django.utils import timezone

class Subject(models.Model):
    etcs_points = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )

    subject = models.CharField(max_length=128)
    max_points = models.IntegerField(default=100)
    lecturer = models.CharField(max_length=128)
    max_etcs = models.IntegerField(choices=etcs_points)

    def __str__(self):
        return self.subject

class Subject_ingredient(models.Model):
    activity_type = (
        ("Lecture", "Lecture"),
        ("Laboratory", "Laboratory"),
        ("Online", "Online"),
    )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    activity = models.CharField(max_length=128, choices=activity_type)
    max_points = models.IntegerField(default=50)
    
    def __str__(self):
        return f'{self.subject} ({self.activity})'

class Task(models.Model):
    answer = (
        ("Yes", "Yes"),
        ("No", "No"),
    )

    subject_ingredient = models.ForeignKey(Subject_ingredient, on_delete=models.CASCADE)
    task = models.CharField(max_length=128)
    returned = models.CharField(max_length=128, choices=answer, default="Yes")
    task_points_scored = models.FloatField()
    task_points_max = models.FloatField(default=0)
    deadline = models.DateTimeField(default=datetime.today, auto_now_add=False, auto_now=False, blank=False)

    def next_task (self):
        return self.returned == "No"

    def __str__(self):
        return f'{self.subject_ingredient}: {self.task}({self.task_points_max})'