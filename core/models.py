from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class Testimony(models.Model):
    author = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null='True')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Testimonies'

    def __str__(self):
        return self.author
