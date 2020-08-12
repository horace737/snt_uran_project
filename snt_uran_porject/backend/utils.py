from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from transliterate import translit


def add_paginator(request, posts, items=7):
    paginator = Paginator(posts, items)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    result = [page, is_paginated, prev_url, next_url]
    return result


def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.title, 'ru', reversed=True))
        instance.slug = slug


def pre_save_seo_description(sender, instance, *args, **kwargs):
    if not instance.seo_description:
        instance.seo_description = instance.description[0:150]
