from django.db.models import Q
from .models import Project, Tag



def searchProject(request):
    search_query = ''
    search_query = request.GET.get('search_query')
    if search_query:
        tag = Tag.objects.filter(name__icontains = search_query)
        projects = Project.objects.distinct().filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) | 
            Q(owner__name__icontains = search_query) |
            Q(tags__in = tag)
            )
    else:  
        search_query=''
        projects = Project.objects.all()    
    return projects, search_query