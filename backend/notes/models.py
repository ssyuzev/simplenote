"""Models for notes app."""

from django.db import models


class Note(models.Model):
    """Note model."""

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
