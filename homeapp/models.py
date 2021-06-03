from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class BlogModel(models.Model):
    name = models.CharField(max_length=250, default='')
    email = models.EmailField(max_length=50, default='')
    subject = models.CharField(max_length=100, default='')
    msg = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='Test')


def __str__(self):
    return self.title