# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-29 13:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', models.TextField(max_length=120, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u043c\u044b\u0441\u043b\u044c)')),
                ('image', models.ImageField(blank=True, default='no-image.png', upload_to='post/', verbose_name='\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=150, unique=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0441\u044b\u043b\u043a\u0438')),
                ('text', models.TextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0430\u0442\u044c\u0438')),
                ('seo_description', models.TextField(max_length=160, verbose_name='SEO \u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c, \u0434\u043e 80 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)')),
                ('view', models.IntegerField(default=0, verbose_name='\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u044b')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('active', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u041f\u043e\u0441\u0442',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u044b',
            },
        ),
    ]
