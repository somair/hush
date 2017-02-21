from django.db import models
from djang.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/hushvids')

class Video(models.Model):
    """
    Base video model
    """

    filename = models.CharField(max_length=255)
    video = models.FileField(storage=fs)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

class Show(models.Model):
    """
    Represents a show
    """

    title = models.CharField(max_length=255)

class Movie(models.Model):
    """
    Respresents a Movie
    """

    title = models.CharField(max_length=255)
    video = models.FileField(storage=fs)
