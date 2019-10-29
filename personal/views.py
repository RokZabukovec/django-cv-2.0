# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.http import FileResponse, Http404
from django.shortcuts import render
from personal.models import Project
from personal.models import ProjectMedia


def index(request):
    featured = Project.objects.filter(featured=True)
    for project in featured:
        project.overview = project.overview[:150] + "..."
    contex = {'featured': featured}
    return render(request, "index.html", contex)


def project(request, pk):
    single = Project.objects.get(pk=pk)
    project_photos = ProjectMedia.objects.filter(project=pk)
    context = {'project': single, 'photos': project_photos}
    return render(request, 'single.html', context)


def projects(request):
    projects = Project.objects.order_by('-posted')
    for project in projects:
        project.overview = project.overview[:150] + "..."
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def download_pdf(request):
    filename = "rok_zabukovec_cv_2019.pdf"
    try:
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "media/" + filename
        abs_file_path = os.path.join(script_dir, rel_path)
        return FileResponse(open(abs_file_path, 'rb'), content_type='application/pdf')
    except OSError:
        raise Http404()
