from django.db import models

class About(models.Model):

    text = models.TextField()


class Ability(models.Model):

    name = models.CharField(max_length= 40)
    value = models.IntegerField()

    time_view = models.CharField(max_length= 4, default= 2)

    def __str__(self):
        return self.name
    
class AbilityInfo(models.Model):

    name = models.CharField(max_length= 40)
    text = models.TextField()

    time_view = models.CharField(max_length= 4, default= 2)

    def __str__(self):
        return self.name
    
class OverView(models.Model):

    working_time = models.IntegerField() 
    completed_projects = models.IntegerField()
    satisfied_customers = models.IntegerField()
    prizes_won = models.IntegerField()
