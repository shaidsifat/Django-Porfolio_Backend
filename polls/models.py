from django.db import models

# Create your models here.
class Contact(models.Model):

    Name =  models.CharField(max_length=30)
    Email =  models.CharField(max_length=30)
    Subject = models.TextField(null=True,blank=True)
    Message = models.TextField(null=True,blank=True)

    def __str__(self):
        return  f"{self.Name}"
