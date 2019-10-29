# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Project(models.Model):
    """Model for storing information about my projects. Posts will be
    presented on the main page in sequence"""

    def __str__(self):
        """String representation of a model"""
        return self.title

    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=9999)
    cover = models.FileField(blank=True)
    link = models.URLField(blank=True)
    posted = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)
    tehnologies = models.CharField(blank=True, max_length=200)


class ProjectMedia(models.Model):
    """Model for storing project photos"""
    image = models.ImageField(blank=True, upload_to='img/')
    posted = models.DateField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        """String representation of a model"""
        return self.project.title
