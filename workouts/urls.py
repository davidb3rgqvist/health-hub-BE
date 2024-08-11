from django.urls import path
from . import views

urlpatterns = [
    path('workoutprograms/', views.WorkoutProgramList.as_view(), name='workoutprogram-list'),
    path('workoutprograms/<int:pk>/', views.WorkoutProgramDetail.as_view(), name='workoutprogram-detail'),
]
