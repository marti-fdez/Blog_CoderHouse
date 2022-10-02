from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User2", verbose_name='Usuario')

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255, blank=True, verbose_name='Mensaje')
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
