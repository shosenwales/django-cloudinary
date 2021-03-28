from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class photos(models.Model):
    Tittle = models.CharField(max_length=100)
    image = CloudinaryField('image')