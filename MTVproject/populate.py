import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MTVproject.settings')

import django
django.setup()


#Fake Pop Script

from MTPapp.models import User
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_first_name=fakegen.first_name()
        fake_last_name=fakegen.last_name()
        fake_email=fakegen.email()
        
        user=User.objects.get_or_create(first_name= fake_first_name,last_name=fake_last_name,email=fake_email)[0]
        user.save()

if __name__=='__main__':
    print('Populating Script')
    populate(20)
    print("population Complete")