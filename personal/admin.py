# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from personal.models import Project
from personal.models import ProjectMedia




# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectMedia)