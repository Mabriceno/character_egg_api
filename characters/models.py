from django.db import models



class Api(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class Universe(models.Model):
    api_id = models.ForeignKey(Api, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    character_api_id = models.IntegerField()
    universe_id = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    egg = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

