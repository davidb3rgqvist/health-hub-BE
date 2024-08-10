from django.db import models
from django.contrib.auth.models import User
from workouts.models import WorkoutProgram


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    workoutprogram = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'workoutprogram']

    def __str__(self):
        return f'{self.owner} {self.post}'