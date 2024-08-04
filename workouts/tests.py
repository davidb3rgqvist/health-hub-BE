from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from datetime import timedelta
from .models import WorkoutProgram, WorkoutSession

class WorkoutProgramTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.workout_program = WorkoutProgram.objects.create(
            owner=self.user, name='Test Program', description='Test Description'
        )

    def test_create_workout_program(self):
        url = reverse('workoutprogram-list')
        data = {'name': 'New Program', 'description': 'New Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WorkoutProgram.objects.count(), 2)
        self.assertEqual(response.data['name'], 'New Program')
        self.assertEqual(response.data['description'], 'New Description')

    def test_get_workout_programs(self):
        url = reverse('workoutprogram-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Program')
        self.assertEqual(response.data[0]['description'], 'Test Description')

class WorkoutSessionTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.workout_program = WorkoutProgram.objects.create(
            owner=self.user, name='Test Program', description='Test Description'
        )
        self.workout_session = WorkoutSession.objects.create(
            workout_program=self.workout_program, name='Test Session', 
            duration=timedelta(minutes=30), date='2024-08-01'
        )

    def test_create_workout_session(self):
        url = reverse('workoutsession-list')
        data = {
            'name': 'New Session',
            'duration': '00:45:00',
            'date': '2024-08-02',
            'workout_program': self.workout_program.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WorkoutSession.objects.count(), 2)
        self.assertEqual(response.data['name'], 'New Session')
        self.assertEqual(response.data['duration'], '00:45:00')
        self.assertEqual(response.data['date'], '2024-08-02')

    def test_get_workout_sessions(self):
        url = reverse('workoutsession-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Session')
        self.assertEqual(response.data[0]['duration'], '00:30:00')
        self.assertEqual(response.data[0]['date'], '2024-08-01')
