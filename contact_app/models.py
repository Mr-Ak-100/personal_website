from django.db import models

class Message(models.Model):

    name = models.CharField(max_length= 35)
    email = models.CharField(max_length= 50)
    phone = models.CharField(max_length= 20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.message[:30]}"
