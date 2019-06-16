# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Tag

admin.site.register(Article)
admin.site.register(Tag)
