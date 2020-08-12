#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from .models import *


def advertisement_list(request):
    advertisement = Advertisement.objects.filter(active=True)
    context = {
        'advertisement': advertisement
    }
    return render(request, 'adv/advertisement-list.html', context=context)
