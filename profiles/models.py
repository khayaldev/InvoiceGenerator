from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from .utils import generate_account_number
# Create your models here.
class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  account_number=models.CharField(max_length=26,blank=True)
  company_name=models.CharField(max_length=220)
  company_info=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  
  avatar=models.ImageField(default='images/avatar.png')
  company_logo=models.ImageField(default='images/no_photo.png')
  
  def __str__(self):
    return f"Profile for a user :{self.user.username}"
  
  def clean(self):
    if(len(self.account_number)!=15 and self.account_number!=""):
      raise ValidationError('Account number must contains 15 characters')
    
  def save(self,*args,**kwargs):
    if self.account_number=="":
      self.account_number=generate_account_number()
    return super().save(*args,**kwargs)
  
