from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE,null= True)
    address= models.CharField(max_length=200)
    phone = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return f'{self.staff.username}-Profile'