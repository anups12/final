from distutils.sysconfig import customize_compiler
from msilib.schema import CustomAction
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer

def Customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.username)
        print('profile created')

post_save.connect(Customer_profile, sender=User)