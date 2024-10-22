
from django.contrib.auth import login
from django.core import paginator
from django.shortcuts import render, redirect

from projects.utils import searchProject, paginationProjects
from .models import Project, Tag
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from .forms import ProjectForm, ReviewForm
from django.contrib import messages

def projects(request):
    #searchProject
    # 1-usul

    # if request.GET.get('search_query'):
    #     search_query = request.GET.get('search_query')

    # tag = Tag.objects.filter(name__icontains = search_query)
    # projects = Project.objects.filter(
    #     Q(title__icontains=search_query) |
    #     Q(description__icontains=search_query) |
    #     Q(owner__name__icontains = search_query) |
    #     Q(tags__in = tag)
    # )
    
    # 2-usul utils.py da 
    projects, search_query = searchProject(request)

    custom_range, projects = paginationProjects(request, projects, 6)

    

    context = {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    
    if request.method == "POST":
       
        form = ReviewForm(request.POST) 
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'Izohingiz muvaffaqiyatli qo\'shildi')
        return redirect('project', pk=projectObj.id)
    context = {'project': projectObj, 'form': form} 
    return render(request, 'projects/single-project.html', context)


# @login_required(login_url='login')
# def createProject(request):
#     profile = request.user.profile
#     form = ProjectForm()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.owner = profile
#             project.save()
#             return redirect('account')
#     context = {"form": form}
#     return render(request, 'projects/project_form.html', context)

# @login_required(login_url='login')
# def updateProject(request, pk):
#     profile = request.user.profile
#     project = profile.project_set.get(id=pk)
#     form = ProjectForm(instance=project)
#     if request.method == 'POST':
#         print(request.POST)
#         newtags = request.POST.get('newtags').replace(',', ' ').split()

#         print(newtags)

#         form = ProjectForm(request.POST, request.FILES, instance=project)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')
#     context = {"form": form}
#     return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)



@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')

    context = {'form': form, 'project': project}
    return render(request, "projects/project_form.html", context)



@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object': project}
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    return render(request, 'delete_template.html', context)





