"""Serializers for notes app."""

from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for NOte model."""

    class Meta:
        """Django magic."""

        model = Note
        fields = ('id', 'title', 'body', 'created_at')
