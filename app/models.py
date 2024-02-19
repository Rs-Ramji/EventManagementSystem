from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    image = models.ImageField(upload_to= "images/")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)
    def __str__(self):
        return self.title