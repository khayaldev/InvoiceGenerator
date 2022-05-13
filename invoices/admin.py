from tkinter.ttk import Widget
from django.contrib import admin
from django.dispatch import receiver
from invoices.models import Invoice, Tag
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin


class TagResource(resources.ModelResource):
  class Meta:
    model=Tag
    fields=('id','name')
    
class TagAdmin(ExportActionMixin,admin.ModelAdmin):
  resource_class=TagResource
  
  
class InvoiceResource(resources.ModelResource):
  profile=Field()
  receiver=Field()
  closed=Field()
  total_amount=Field()
  positions=Field()
  class Meta:
    model=Invoice
    export_order=('id','profile','receiver','number',
                  'completion_date','issue_date','payment_date','created','closed')
    widgets={
    'completion_date': {'format': '%d.%m.%Y'},
    'issue_date': {'format': '%d.%m.%Y'},
    'payment_date': {'format': '%d.%m.%Y'},
    'created': {'format': '%d.%m.%Y'},
    }
    
  def dehydrate_profile(self,obj):
    return obj.profile.user.username
  
  def dehydrate_receiver(self,obj):
    return obj.receiver.name
  
  def dehydrate_closed(self,obj):
    if obj.closed:
      return "True"
    return "False"
  
  def dehydrate_total_amount(self,obj):
    return obj.total_amount
  
  def dehydrate_positions(self,obj):
    listpositions=[x.title for x in obj.positions]
    return ', '.join(listpositions)
    
      
    
  
    
class InvoiceAdmin(ExportActionMixin,admin.ModelAdmin):
  resource_class=InvoiceResource



# Register your models here.
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Tag,TagAdmin)
