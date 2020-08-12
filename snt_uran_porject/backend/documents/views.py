#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from itertools import chain
from .models import *


def get_estimates(request):
    estimate = Estimate.objects.all()[:3]
    context = {
        'estimate': estimate
    }
    return render(request, 'documents/estimates.html', context=context)


def snt_regulations(request):
    category = get_object_or_404(Category, title=u'Устав')
    docs = Document.objects.filter(category=category, archive=False)
    context = {
        'docs': docs
    }
    return render(request, 'documents/snt-regulations.html', context=context)


def snt_provisions(request):
    category = get_object_or_404(Category, title=u'Положения')
    docs = Document.objects.filter(category=category, archive=False)
    context = {
        'docs': docs
    }
    return render(request, 'documents/snt-provisions.html', context=context)


def snt_meeting(request):
    category = get_object_or_404(Category, title=u'Протоколы общих собраний')
    docs = Document.objects.filter(category=category, archive=False)
    context = {
        'docs': docs
    }
    return render(request, 'documents/snt-meeting.html', context=context)


def snt_government(request):
    category = get_object_or_404(
        Category, title=u'Протоколы заседаний правления')
    docs = Document.objects.filter(category=category, archive=False)
    context = {
        'docs': docs
    }
    return render(request, 'documents/snt-government.html', context=context)


def get_laws(request):
    category = get_object_or_404(Category, title=u'Законодательство')
    docs = Document.objects.filter(category=category, archive=False)
    context = {
        'docs': docs
    }
    return render(request, 'documents/laws.html', context=context)


def info_control(request):
    category = get_object_or_404(Category, title=u'Управление')
    content = Content.objects.filter(category=category)
    context = {
        'content': content
    }
    return render(request, 'documents/info-control.html', context=context)


def info_requisites(request):
    category = get_object_or_404(Category, title=u'Реквизиты')
    content = Content.objects.filter(category=category)
    context = {
        'content': content
    }
    return render(request, 'documents/info-requisites.html', context=context)


def info_plan(request):
    category = get_object_or_404(Category, title=u'План СНТ')
    docs = Document.objects.filter(category=category, archive=False)
    context = {
        'docs': docs
    }
    return render(request, 'documents/info-plan.html', context=context)


def get_gallery(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery
    }
    return render(request, 'documents/gallery.html', context=context)


def get_archive(request):
    docs = Document.objects.filter(archive=True)
    archive = Archive.objects.all()
    archive = list(chain(docs, archive))
    context = {
        'archive': archive
    }
    return render(request, 'documents/archive.html', context=context)
