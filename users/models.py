from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pic.jpg', upload_to='profile_pics', blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

# Create your models here.
