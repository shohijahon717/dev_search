
from django.contrib.auth import login
from django.core import paginator
from django.shortcuts import render, redirect

from projects.utils import searchProject, paginationProjects
from .models import Project, Tag
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from .forms import ProjectForm


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
    print(projects)
    custom_range, projects = paginationProjects(request, projects, 2)
    print(projects)
    

    context = {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project': projectObj}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {"form": form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {"form": form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object': project}
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    return render(request, 'delete_template.html', context)





