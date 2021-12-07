from django.shortcuts import render, redirect
from django.urls.conf import path
from .models import Profile, Skill
from django.contrib.auth.models import User    

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .forms import CustomUserCreationForm

# Create your views here.


def loginUser(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f'Foydalanuvchi nomi topilmadi')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Tizimga muvaffaqiyatli kirdingiz!')
            return redirect('profiles')
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol xato")

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'Foydalanuvchi tizimdan chiqdi!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'Foydalanuvchi hisobi yaratildi!')
            return redirect('login')


        else:
            messages.success(request, 'Ro\'yxatdan o\'tishda xatolik yuz berdi!')

    context = {'page': page, 'form': form}  
    return render(request, 'users/login_register.html', context)


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



@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context={'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)
