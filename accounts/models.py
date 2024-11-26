from django.db import models

# Create your models here.

class Feedback(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    fecha = models.DateTimeField(auto_now_add=True)