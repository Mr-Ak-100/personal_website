from django.db import models

class Education(models.Model):
    
    start_time = models.IntegerField()
    end_time = models.CharField(max_length= 6)

    name = models.CharField(max_length= 30)
    company = models.CharField(max_length= 30)

    info = models.TextField()

    def __str__(self):
        return self.name
    
class Experience(models.Model):

    start_time = models.IntegerField()
    end_time = models.CharField(max_length= 6)

    name = models.CharField(max_length= 30)
    company = models.CharField(max_length= 30)

    info = models.TextField()

    def __str__(self):
        return self.name
    