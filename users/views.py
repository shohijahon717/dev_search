from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib.auth.models import User    

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import  messages

# Create your views here.


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f'{username} nomli foydalanuvchi topilmadi')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol xato")

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def profiles(request):
    user_profiles = Profile.objects.all()

    context = {'profiles': user_profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact='')  # description bo'sh bo'lganini olmaydi
    # exclude-istisno
    otherSkills = profile.skill_set.filter(description='')

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)
