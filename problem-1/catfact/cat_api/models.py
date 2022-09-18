from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catfact(models.Model):
    fact = models.CharField(max_length=200)
    length = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.fact