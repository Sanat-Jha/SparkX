from django.db import models

# Create your models here.
class User(models.Model):
    Id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=500)
    Second_name = models.CharField(max_length=500)
    Username = models.CharField(max_length=500)
    Email = models.EmailField()
    Verified = models.BooleanField(default=False)
    Bio = models.TextField(blank=True,default="")
    Dp = models.ImageField(upload_to="DPs")
    Points = models.IntegerField(default=0)
    Notifications = models.JSONField(blank=True,default="{}")
    def __str__(self):
        return self.Username

class Post(models.Model):
    Id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Posts")
    Owner = models.CharField(max_length=500)
    Comments = models.JSONField()
    date = models.DateTimeField()
    likes = models.JSONField()
    saved = models.JSONField()
    Caption = models.TextField()
    def __str__(self):
        return self.Owner