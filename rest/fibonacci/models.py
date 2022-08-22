from django.db import models

class Fibonacci(models.Model):
    total = models.SmallIntegerField()
    resultado = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']