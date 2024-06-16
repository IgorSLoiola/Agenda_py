from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    name = models.CharField(max_length=110)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d' ,blank=True , null=True)
    category = models.ForeignKey(
        Category,
        on_delete= models.SET_NULL,
        blank=True, null=True
    )

    owner = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.name}'