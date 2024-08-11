from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from HealthHub_BE.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        workoutprogram_count=Count('owner__workoutprogram', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = []
    ordering_fields = [
        'workoutprogram_count',
    ]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        workoutprogram_count=Count('owner__workoutprogram', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
