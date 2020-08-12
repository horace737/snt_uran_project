#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from utils import pre_save_slug, pre_save_seo_description

from PIL import Image


class Post(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name=u'Пользователь',
        on_delete=models.CASCADE
        )
    title = models.CharField(u'Заголовок', max_length=50, db_index=True)
    description = models.TextField(u'Описание (Главная мысль)', max_length=120)
    image = models.ImageField(
        u'Главное изображение',
        upload_to='post/',
        default='no-image.png',
        blank=True
        )
    slug = models.SlugField(
        u'Текст ссылки',
        blank=True,
        max_length=150,
        unique=True,
        editable=False
        )
    text = models.TextField(u'Текст статьи', blank=True)
    seo_description = models.TextField(
        u'SEO Описание (для поисковых систем, до 80 символов)',
        max_length=160
        )
    view = models.IntegerField(u'Просмотры', default=0)
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    active = models.BooleanField(u'Опубликован', default=True)

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

pre_save.connect(pre_save_slug, sender=Post)
pre_save.connect(pre_save_seo_description, sender=Post)
