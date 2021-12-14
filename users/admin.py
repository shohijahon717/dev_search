from django.contrib import admin
from django.contrib.auth.models import User 
from .models import Profile, Skill, Message

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
