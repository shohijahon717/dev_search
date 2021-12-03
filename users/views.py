from django.shortcuts import render, redirect
from .models import Profile, Skill, Users
from django.contrib.auth import login, authenticate


# Create your views here.


def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Users.objects.get(username=username)
        except:
            print(f'{username} nomli foydalanuvchi topilmadi')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print("Foydalanuvchi nomi yoki parol xato")

    return render(request, 'users/login_register.html')


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
