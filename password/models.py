from django.db import models

# Create your models here.
class Password(models.Model):
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.password