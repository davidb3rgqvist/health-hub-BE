from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import WorkoutProgram
from .serializers import WorkoutProgramSerializer
from HealthHub_BE.permissions import IsOwnerOrReadOnly

class WorkoutProgramList(generics.ListCreateAPIView):
    serializer_class = WorkoutProgramSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = WorkoutProgram.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
        'likes__owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WorkoutProgramDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a workout program.
    """
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer
    permission_classes = [IsOwnerOrReadOnly]