from django.db import models

# Create your models here.
class Prediction(models.Model):
    name = models.CharField(max_length=100)
    id_transport = models.PositiveBigIntegerField()
    
