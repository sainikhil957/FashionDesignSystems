from django.db import models

# Create your models here.
class Fdsignup(models.Model):
    firstname=models.CharField(max_length=100,blank=False)
    lastname=models.CharField(max_length=100,blank=False)
    phoneno=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    experience=models.CharField(max_length=100,blank=False)
    designation=models.CharField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="fdsignup_table"



class Fdform(models.Model):
    clothname=models.CharField(max_length=100,blank=False,default=None)
    clothfile=models.ImageField(upload_to='media/image',default='')
    clothgender=models.CharField(max_length=100,blank=False,default=None)
    clothtype=models.CharField(max_length=100,blank=False)
    clothcolour=models.CharField(max_length=100,blank=False)
    clothpattern=models.CharField(max_length=100,blank=False)
    clothsizes=models.CharField(max_length=100,blank=False)
    clothprice=models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True,default=None)
    username=models.CharField(max_length=100,blank=False,default=None)
    email=models.CharField(max_length=100,blank=False,default=None)
    class Meta:
        db_table="fdform_table"
