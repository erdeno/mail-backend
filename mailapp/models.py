# We are importing user from auth models
from django.contrib.auth.models import User

from django.db import models


class Email(models.Model):
    sender = models.ForeignKey(User, related_name='senders', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receivers", on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
