#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.static import serve

from adv.views import *
from blog.views import *
from documents.views import *
from common.views import *
from forum.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', posts_list, name='posts_list'),
    url(r'post/(?P<slug>[-\w]+)/$', post_detail, name='post_detail'),

    url(r'^documents/$', DocumentsView.as_view(), name='documents'),
    url(r'^information/$', InformationView.as_view(), name='information'),
    url(r'^live/$', LiveView.as_view(), name='live'),
    url(r'^estimates/$', get_estimates, name='estimates'),

    url(r'^documents/snt/$', SntView.as_view(), name='snt'),
    url(r'^documents/laws/$', get_laws, name='laws'),

    # Устав
    url(r'^documents/snt/regulations/$', snt_regulations, name='regulations'),
    # Положения
    url(r'^documents/snt/provisions/$', snt_provisions, name='provisions'),
    # Общие собрания
    url(r'^documents/snt/meeting/$', snt_meeting, name='meeting'),
    # Правление
    url(r'^documents/snt/government/$', snt_government, name='government'),

    # Управление
    url(r'^information/control$', info_control, name='info_control'),
    # Реквизиты
    url(r'^information/requisites$', info_requisites, name='info_requisites'),
    # План СНТ
    url(r'^information/plan$', info_plan, name='info_plan'),

    # Галерея
    url(r'^live/gallery$', get_gallery, name='gallery'),
    # Объявления
    url(r'^live/advertisement$', advertisement_list, name='advertisement'),
    # Архив
    url(r'^live/archive$', get_archive, name='archive'),

    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^media/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',
        serve, {'document_root': settings.STATIC_ROOT}),

    url(r'^forum/', get_forum, name='forum'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
