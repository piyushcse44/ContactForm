from django.db import models


# Create your models here.


class ContactForm(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    Name = models.CharField(max_length=100,default="Enter Your Name")
    Email = models.EmailField(max_length=100,default="xyz@gmail.com")
    Phone = models.CharField(max_length=10,default='0123456789')
    Adress = models.CharField(max_length=200,default='xyz nagar')
    Message_Subject = models.CharField(max_length=1000,verbose_name="Message Subject")
    Message = models.TextField(null=True,blank = True)

    def __str__(self):
        return self.Name