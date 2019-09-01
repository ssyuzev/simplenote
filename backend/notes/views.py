"""Views for notes app."""

from rest_framework import viewsets

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet for Note model."""

    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
