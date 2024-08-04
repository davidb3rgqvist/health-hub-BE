from django.db import models
from django.contrib.auth.models import User

class WorkoutProgram(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class WorkoutSession(models.Model):
    workout_program = models.ForeignKey(WorkoutProgram, related_name='sessions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.DurationField()
    date = models.DateField()
