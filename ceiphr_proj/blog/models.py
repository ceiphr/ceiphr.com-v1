# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField
import datetime


class Tag(models.Model):
    name = models.CharField(default="", max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(default="", max_length=255)
    summary = models.CharField(default="", max_length=160)
    short_url = models.CharField(blank=True, default="", max_length=255)

    public = models.BooleanField(default=False)
    latex_support = models.BooleanField(default=False)

    slug = models.SlugField(blank=True)
    body = models.TextField(default="", max_length=20000)
    read_time = models.IntegerField(default=0)

    image = ImageField(upload_to="articles/%Y/%m/%d")

    modified = models.DateField(default=datetime.date.today)
    published = models.DateField(default=datetime.date.today)

    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        wpm = 265  # Average amount of words read per minute
        wl = 5  # Average word length
        time = len(self.body) // (wpm * wl)

        if time == 0:
            self.read_time = 1
        else:
            self.read_time = time

        if not self.id:
            self.slug = slugify(self.title)
            self.short_url = "https://www.ceiphr.com/blog/%s" % self.slug
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/blog/%s/" % self.slug

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title
