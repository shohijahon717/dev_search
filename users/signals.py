from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User 


def createProfile(sender, instance, created, **kwargs):

    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email = user.email,
            name=user.first_name
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        if not profile.name:
            user.first_name = ""
        else:
            user.first_name = profile.name
        user.username = profile.username
        if not profile.email:
            user.email = ''
        else:
            user.email = profile.email
        user.save()



def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
        


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
