from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutProgramViewSet, WorkoutSessionViewSet

router = DefaultRouter()
router.register(r'workoutprograms', WorkoutProgramViewSet, basename='workoutprogram')
router.register(r'workoutsessions', WorkoutSessionViewSet, basename='workoutsession')

urlpatterns = [
    path('', include(router.urls)),
]
