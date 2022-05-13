from operator import inv
from django.db import models

from invoices.models import Invoice

# Create your models here.

class Position(models.Model):
  invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
  title=models.CharField(max_length=200)
  description=models.TextField(help_text='Optional Text',blank=True)
  amount=models.FloatField(help_text='in US $')
  created=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'Invoice : {self.invoice.number}, position title:{self.title}'