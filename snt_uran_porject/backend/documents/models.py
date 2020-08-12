#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from utils import pre_save_slug
from django.db import models

from PIL import Image


class Category(models.Model):
    title = models.CharField(u'Название раздела', max_length=350)
    slug = models.SlugField(
        u'Текст ссылки',
        blank=True,
        max_length=350,
        unique=True,
        editable=False
        )
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Раздел'
        verbose_name_plural = u'Разделы'
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('category_posts', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)


class Document(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name=u'Раздел',
        on_delete=models.CASCADE
        )
    title = models.CharField(u'Название документа', max_length=350)
    document = models.FileField(u'Документ', upload_to='docs/')
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    archive = models.BooleanField(u'В архив', default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = u'Документ'
        verbose_name_plural = u'Документы'
        ordering = ('order',)

    def __unicode__(self):
        return unicode(self.title)


class Content(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name=u'Раздел',
        on_delete=models.CASCADE
        )
    title = models.CharField(u'Заголовок контента', max_length=350)
    text = models.TextField(u'Текст', blank=True)
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Контент'
        verbose_name_plural = u'Контент'

    def __unicode__(self):
        return unicode(self.title)


class Gallery(models.Model):
    title = models.CharField(u'Описание изображения', max_length=350)
    image = models.ImageField(
        u'Изображение',
        upload_to='gallery/',
    )
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Галерея'
        verbose_name_plural = u'Галерея'

    def __unicode__(self):
        return unicode(self.title)


class Estimate(models.Model):
    title = models.CharField(u'Название', max_length=350)
    plan = models.FileField(u'План', upload_to='estimate/')
    execution = models.FileField(
        u'Исполнение',
        upload_to='estimate/',
        blank=True
    )
    archive = models.BooleanField(u'В архив', default=False)
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = u'Смета'
        verbose_name_plural = u'Смета'
        ordering = ('order',)

    def __unicode__(self):
        return unicode(self.title)


class Archive(models.Model):
    title = models.CharField(u'Название документа', max_length=350)
    document = models.FileField(u'Документ', upload_to='archive/')
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Архив'
        verbose_name_plural = u'Архив'

    def __unicode__(self):
        return unicode(self.title)

pre_save.connect(pre_save_slug, sender=Category)
