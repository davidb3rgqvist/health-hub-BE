from django.db import models
from django.contrib.auth.models import User
from workouts.models import WorkoutProgram

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    workoutprogram = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
