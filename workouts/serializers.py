from rest_framework import serializers
from .models import WorkoutProgram, WorkoutSession
from profiles.serializers import ProfileSerializer

class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = ['id', 'name', 'duration', 'date', 'workout_program']

class WorkoutProgramSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    sessions = WorkoutSessionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutProgram
        fields = ['id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'name', 'description', 'created_at', 'sessions']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            return obj.owner == request.user
        return False
