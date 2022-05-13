from django.db import models
from profiles.models import Profile
from receivers.models import Receiver
from .utils import generate_invoice_number
# Create your models here.

class Tag(models.Model):
  name=models.CharField(max_length=200)
  def __str__(self):
    return self.name
  
  
class Invoice(models.Model):
  profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
  receiver=models.ForeignKey(Receiver,on_delete=models.CASCADE)
  number=models.CharField(max_length=150,blank=True)
  completion_date=models.DateField()
  issue_date=models.DateField()
  payment_date=models.DateField()
  created=models.DateTimeField(auto_now_add=True)
  #if closed hide add positions and unable adding new ones
  closed=models.BooleanField(default=False)
  tags=models.ManyToManyField(Tag,blank=True)
  
  def __str__(self):
    return f'Invoice number {self.number}, pk:{self.pk}'
  
  @property
  def tags(self):
    return self.tags.all()
  
  @property
  def positions(self):
    return self.position_set.all()
  
  @property
  def total_amount(self):
    total=0
    positions=self.positions
    for pos in positions:
      total+=pos.amount
    return round(total,2)
  
  def save(self,*args,**kwargs):
    if self.number=="":
      self.number=generate_invoice_number()
    return super().save(*args,**kwargs)