from django.contrib import admin
from positions.models import Position
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
# Register your models here.

class PositionResource(resources.ModelResource):
  invoice=Field()
  description=Field()
  
  
  class Meta:
    model=Position
    fields=('invoice','title','description','amount','created')

  def dehydrate_invoice(self,obj):
    print(obj)
    return obj.invoice.number

  def dehydrate_description(self,obj):
    if obj.description=="":
      return "-"
    return obj.description

class PositionAdmin(ExportActionMixin,admin.ModelAdmin):
  resource_class=PositionResource
  

admin.site.register(Position,PositionAdmin)