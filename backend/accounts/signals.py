from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
User = get_user_model()

def updateUser(sender,instance, **kwargs):
    print('signal')
    user = instance
    if user.email != '':
        user.name = user.email
        
    print('Signal Triggered')

    pre_save.connect(updateUser,sender=User)