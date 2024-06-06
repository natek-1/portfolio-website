from django.shortcuts import render, get_list_or_404
from .models import Project, Tag

def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")

def project(request, id):
    project = get_list_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})

