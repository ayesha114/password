from django.db import models

class GeneratedPassword(models.Model):
    password = models.CharField(max_length=100)
    date_generated = models.DateTimeField(auto_now_add=True)