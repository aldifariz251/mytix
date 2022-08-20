from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, null= True)
    email = models.CharField(max_length=100, null= True)
    password = models.CharField(max_length=100, null= True)

    class Meta: 
        db_table = "User"
        verbose_name = "User App"

    def __str__(self):
        return self.username
