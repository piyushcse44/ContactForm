from django.db import models


# Create your models here.


class ContactForm(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    Name = models.CharField(max_length=100,default="")
    Email = models.EmailField(max_length=100,default="")
    photo = models.ImageField(default = "Screenshot from 2022-06-17 08-43-48.png")
    Phone = models.CharField(max_length=10,default='')
    Adress = models.CharField(max_length=200,default='')
    Message_Subject = models.CharField(max_length=1000,verbose_name="Message Subject")
    Message = models.TextField(null=True,blank = True)

    def __str__(self):
        return self.Name
