from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Subject_ingredient, Subject
from django.utils import timezone
import datetime

def index(request):
    def next_tazk(Task):
        closest_task = datetime.timedelta(days=30)

        for task in Task:

            #comparison closest_task to next task
            task_closest = task.deadline - timezone.now() < closest_task 

            if task.returned == "No" and task_closest:
                closest_task = task.deadline - timezone.now()
                closest = task
        
        return closest

    def points_from_subject(Task, Subject_ingredient):
        points = 0

        for task in Task:
            if task.subject_ingredient == Subject_ingredient.get(pk=2):
                points += task.task_points_scored
        return points

    def subiekt(Subject):
        lista = []
        for subject in Subject:
            lista.append(subject)

        return lista

    def punkty(Task, Subject_ingredient):
        lista = []

        for subject in Subject_ingredient:
            points = 0
            for task in Task:
                if task.subject_ingredient == subject:
                    points += task.task_points_scored
            lista.append(points)
        
        return lista

    return render(request, "school/index.html", {
        'next_tasks': next_tazk(Task.objects.all()),
        'Task': Task.objects.all(),
        'Subject': Subject_ingredient.objects.all(),
        'Punkty': punkty(Task.objects.all(), Subject_ingredient.objects.all())
    })