#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class AdvertisementAdmin(SummernoteModelAdmin):
    summernote_fields = ('text', )

admin.site.register(Advertisement, AdvertisementAdmin)
