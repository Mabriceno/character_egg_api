from django.db import models
from characters.models import Character



class WinEvent(models.Model):
    winner_name = models.CharField(max_length=100)
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
