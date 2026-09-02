from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Challenge
from .serializers import ChallengeSerializer


class ChallengeListCreateView(generics.ListCreateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Challenge.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)