from django.db import models
from django.conf import settings

class Message(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('Smart assistant', 'Smart Assistant'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} | {self.user.username} | {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

