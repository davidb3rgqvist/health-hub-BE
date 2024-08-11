from django.db import models
from django.contrib.auth.models import User
from workouts.models import WorkoutProgram

class Like(models.Model):
    workout_program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, related_name='likes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_given')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'workout_program']

    def __str__(self):
        return f'{self.owner} likes {self.workout_program}'
