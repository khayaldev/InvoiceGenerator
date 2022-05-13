from django import forms
from .models import Invoice
from django.core.exceptions import ValidationError
class InvoiceForm(forms.ModelForm):
  completion_date=forms.DateField(widget=(forms.DateInput(attrs={'type':'date'})))
  issue_date=forms.DateField(widget=(forms.DateInput(attrs={'type':'date'})))
  payment_date=forms.DateField(widget=(forms.DateInput(attrs={'type':'date'})))
  class Meta:
    model=Invoice
    fields=('receiver',
            'number',
            'completion_date',
            'issue_date',
            'payment_date',
            )
  
  def clean_number(self):
    number=self.cleaned_data['number']
    if len(number)<10 and number!="":
      raise ValidationError('Number is too short')
    return number
  
