from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutProgramViewSet, WorkoutSessionViewSet

router = DefaultRouter()
router.register(r'workoutprograms', WorkoutProgramViewSet)
router.register(r'workoutsessions', WorkoutSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]