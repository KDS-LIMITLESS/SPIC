from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  
    
# Overiding the save method so as to add some other functionality
    def save(self):
        super().save() #save method of parent class

        #grab the image the parent class saved and resize it
        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 350:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



        