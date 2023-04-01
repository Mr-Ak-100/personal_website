from django.db import models

class Info(models.Model):

    website_title = models.CharField(max_length= 50)
    
    name = models.CharField(max_length= 15)
    lname = models.CharField(max_length= 15)

    country = models.CharField(max_length= 12)
    city = models.CharField(max_length= 12)
    district = models.CharField(max_length= 12)

    email = models.EmailField()
    number = models.CharField(max_length= 15)
    address = models.TextField()

class MainText(models.Model):

    text = models.CharField(max_length= 50)

    def __str__(self):
        return self.text

class Logo(models.Model):

    website_icon = models.ImageField()
    desktop_logo = models.ImageField()
    mobile_logo = models.ImageField()

class Social(models.Model):

    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

