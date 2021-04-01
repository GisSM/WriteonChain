from django.db import models
from django.contrib.auth.models import User

class User_ip(models.Model):
    utente = models.OneToOneField(User, on_delete=models.CASCADE)
    ip=models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return self.utente.username
