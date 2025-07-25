from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_seat_format

from config import settings


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateTimeField()
    actors = models.TextField(help_text="Actor list, plain text")

    def __str__(self) -> str:
        return f"{self.title} ({self.date.strftime('%Y-%m-%d %H:%M')})"


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seat = models.CharField(max_length=5, validators=[validate_seat_format])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'seat')

    def __str__(self) -> str:
        return f"{self.user.username} - {self.event.title} - {self.seat}"
