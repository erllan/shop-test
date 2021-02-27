from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    key = models.CharField(max_length=255, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', default=None, blank=True,
                               null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    photo = models.ImageField(upload_to='product/photo/', null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title

    def default_photo(self):
        return "static/image/default.png"
