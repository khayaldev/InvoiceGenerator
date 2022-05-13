from django.contrib import admin
from receivers.models import Receiver
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
# Register your models here.

class ReceiverResources(resources.ModelResource):
  class Meta:
    fields=('name','address','website','create')
    export_order=('name','website','create','address')


class ReceiverAdmin(ExportActionMixin,admin.ModelAdmin):
  resource_class=ReceiverResources

admin.site.register(Receiver,ReceiverAdmin)