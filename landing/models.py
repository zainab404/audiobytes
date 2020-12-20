from django.db import models
from django import forms

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=264)
    category = models.CharField(max_length=264)
    duration = models.DurationField()

class AudioFeedback(models.Model):
    name = models.CharField(max_length=264, default="")
    feedback = models.CharField(max_length=264, default="")

    def __str__(self):
        return self.name


