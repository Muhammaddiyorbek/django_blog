from django.db import models

class Catagory(models.Model):
    nomi=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.nomi

class Post(models.Model):
    tanlov=models.ForeignKey(Catagory,on_delete=models.CASCADE,null=True,blank=True)
    nomi=models.CharField(max_length=255,null=True,blank=True)
    rasm=models.ImageField(upload_to='rasmlar',null=True,blank=True)

    def __str__(self):
        return self.nomi