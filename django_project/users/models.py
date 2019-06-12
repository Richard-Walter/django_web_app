from django.db import models
from django.contrib.auth.models import User

# need to register this new model within the admin file of our app


class Profile(models.Model):
    # extend the default user model by adding image
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user} Profile'
