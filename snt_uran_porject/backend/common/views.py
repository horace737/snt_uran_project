#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class DocumentsView(TemplateView):
    template_name = "common/documents.html"


class SntView(TemplateView):
    template_name = "common/snt.html"


class InformationView(TemplateView):
    template_name = "common/information.html"


class LiveView(TemplateView):
    template_name = "common/live.html"
