from django.db import models
from django.contrib.auth.models import User

class WorkoutProgram(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='workout_program_images/', default='../default_workout_program', blank=True)
    likes = models.ManyToManyField(User, through='Like', related_name='liked_workout_programs')
    comments = models.ManyToManyField(User, through='Comment', related_name='commented_workout_programs')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
