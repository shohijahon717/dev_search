from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile, Users

# @receiver(post_save, sender=Profile)


def createProfile(sender, instance, created, **kwargs):
    print("Profile signal triggered")
    if created:
        users = instance
        profile = Profile.objects.create(
            user=users,
            username=users.username,
            email=users.email,
            name=users.first_name
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('Deleting User...')


post_save.connect(createProfile, sender=Users)
post_delete.connect(deleteUser, sender=Profile)
