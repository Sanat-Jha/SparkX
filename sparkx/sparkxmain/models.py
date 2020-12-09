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
    Dp = models.ImageField(upload_to="DPs", default="static/media/Dps/profileicon.png")
    Points = models.IntegerField(default=0)
    Notifications = models.JSONField(blank=True,default=[])
    Followers = models.JSONField(blank=True,default=[])
    Following = models.JSONField(blank=True,default=[])
    Postlist = models.JSONField(blank=True,default=[])
    def __str__(self):
        return self.Username + " " + str(self.Id)

class Post(models.Model):
    Id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Posts")
    Owner = models.CharField(max_length=500)
    Comments = models.JSONField(blank=True,default=[])
    date = models.DateTimeField(auto_now=True)
    likes = models.JSONField(blank=True,default=[])
    saved = models.JSONField(blank=True,default=[])
    Caption = models.TextField()
    Status = models.CharField(max_length=500,default="Active") #active archieved deleted
    def __str__(self):
        return self.Caption + " " + str(self.Id)