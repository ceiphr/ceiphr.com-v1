# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.views.generic import TemplateView
from django.http import Http404

from .models import Article
from portfolio.models import Profile


class GetLargeFeed(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            "articles": Article.objects.exclude(public=False),
            "title": "Ari Birnbaum, %s" % Profile.objects.first().slogan,
            "is_feed": True,
            "slogan": Profile.objects.first().slogan,
            "desc": Profile.objects.first().desc,
            "avatar": Profile.objects.first().logo,
            "resume_url": Profile.objects.first().resume_url,
            "favicon": Profile.objects.first().favicon,
            "debug": int(os.getenv('DEBUG', default=1)),
        }
        return context


class GetArticle(TemplateView):
    template_name = "blog/article.html"

    def get_context_data(self, slug, *args, **kwargs):
        try:
            article_exists = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            article_exists = None

        if article_exists:
            context = {
                "article": Article.objects.get(slug=slug),
                "is_article": True,
                "tags": Article.objects.get(slug=slug).tags.all(),
                "recs": Article.objects.exclude(public=False)
                .exclude(slug=slug),
                "title": Article.objects.get(slug=slug).title,
                "avatar": Profile.objects.first().logo,
                "resume_url": Profile.objects.first().resume_url,
                "favicon": Profile.objects.first().favicon,
                "debug": int(os.getenv('DEBUG', default=1)),
            }
        else:
            raise Http404

        return context


class GetFeed(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self, *args, **kwargs):
        tag = self.request.GET.get("tag", "")

        context = {
            "is_feed": True,
            "desc": "Articles about computer science \
                and technology from Ari Birnbaum.",
            "avatar": Profile.objects.first().logo,
            "resume_url": Profile.objects.first().resume_url,
            "favicon": Profile.objects.first().favicon,
            "debug": int(os.getenv('DEBUG', default=1)),
        }

        if tag:
            context["tag"] = tag
            context["title"] = tag
            context["articles"] = Article.objects \
                .filter(tags__name=tag) \
                .exclude(public=False)

            if not Article.objects \
                    .filter(tags__name=tag).exclude(public=False):
                raise Http404
        else:
            context["title"] = "All Articles"
            context["articles"] = Article.objects.exclude(public=False)

        return context
