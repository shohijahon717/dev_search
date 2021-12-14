from django.db import models

import uuid
from django.contrib.auth.models import AbstractUser, User 

from django.conf import settings
from django.db.models.fields import BooleanField, EmailField
# Create your models here.


User._meta.get_field('email')._unique = True

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # on_delete=models.CASCADE - models.CASCADE Users uchsa profile ham uchishini korsaadi, null = True - malumotlar bazasida ustunni bo'sh qoldirishga ruxsat beradi, blank=True- formalarda to'ldirmay ketish mumkinligini bildiradi
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_telegram = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)  # fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile,
                              null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)  # fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']










