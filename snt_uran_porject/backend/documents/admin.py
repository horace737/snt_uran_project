#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


admin.site.register(Category)

admin.site.register(Gallery)

admin.site.register(Archive)


class ContentAdmin(SummernoteModelAdmin):
    summernote_fields = ('text', )
admin.site.register(Content, ContentAdmin)


@admin.register(Document)
class DocumentAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Document
    list_display = ['title', 'created', ]


@admin.register(Estimate)
class EstimateAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Document
