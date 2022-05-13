import profile
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
  print('Triggered')
  if created:
    Profile.objects.create(user=instance)
    
    
@receiver(post_delete,sender=Profile)
def delete_profile(sender,instance,**kwargs):
  user=instance.user
  user.delete()
