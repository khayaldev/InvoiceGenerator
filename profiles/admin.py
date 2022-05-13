from django.contrib import admin
from profiles.models import Profile
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field


class ProfileResources(resources.ModelResource):
  user=Field()
  class Meta:
    model=Profile
    fields=('id','user','account_number','company_name','company_info','created_at','updated_at')
    export_order = ('id', 'account_number', 'user', 'company_name','company_info','created_at','updated_at')

    widgets = {
                'created_at': {'format': '%d.%m.%Y'},
                'updated_at': {'format': '%d.%m.%Y'},
                }
  def dehydrate_user(self,obj):
    return obj.user.username
    

class ProfileAdmin(ExportActionMixin,admin.ModelAdmin):
  resource_class=ProfileResources
# Register your models here.
admin.site.register(Profile,ProfileAdmin)