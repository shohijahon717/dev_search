from django.shortcuts import render
from .models import Profile, Skill
# Create your views here.


def profiles(request):
    user_profiles = Profile.objects.all()
    context = {'profiles': user_profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)
