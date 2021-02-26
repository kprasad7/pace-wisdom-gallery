from django.db import models

# Create your models here.
class Imagee(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    category = [
        ('a',"A"),
        ('b' , "B"),
        ('c', 'C'),
    ]
    category=models.CharField(max_length=10,choices=category,default='a')

        
    def __str__(self):
        return self.caption