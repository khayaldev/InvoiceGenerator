from django.shortcuts import render
from invoices.models import Invoice
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):

  
  return render(request,'home.html',{})