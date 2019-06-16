# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from sentry_sdk import capture_message, last_event_id

from .models import Article
from django.conf import settings
from portfolio.models import Profile


# Error catching with full page - 404
def handler404(request, exception, template_name="prompt.html"):
    context = {
        "title": "404",
        "prompt": "Page not found.",
        "desc": "Page not found.",
        "error": True,
        "rain_fall": range(20),
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
        "debug": settings.DEBUG,
    }
    capture_message("Page not found!", level="error")
    return render(request, "prompt.html", context, status=404)


# Error catching with full page - 500
def handler500(request, *args, **argv):
    context = {
        "title": "500",
        "prompt": "Internal Server Error.",
        "desc": "Internal Server Error.",
        "error": True,
        "rain_fall": range(20),
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
        "debug": settings.DEBUG,
    }
    capture_message("Internal Server Error!", level="error")
    return render(
        request,
        "prompt.html",
        {"sentry_event_id": last_event_id()},
        context,
        status=500,
    )


class GetLargeFeed(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            "articles": Article.objects.exclude(public=False),
            "title": "Ari Birnbaum",
            "is_feed": True,
            "rain_fall": range(20),
            "slogan": Profile.objects.first().slogan,
            "desc": Profile.objects.first().desc,
            "avatar": Profile.objects.first().logo,
            "resume_url": Profile.objects.first().resume_url,
            "favicon": Profile.objects.first().favicon,
            "debug": settings.DEBUG,
        }

        return context


class GetArticle(TemplateView):
    template_name = "article.html"

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
                "debug": settings.DEBUG,
            }
        else:
            raise Http404

        return context


class GetFeed(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, *args, **kwargs):
        tag = self.request.GET.get("tag", "")

        context = {
            "is_feed": True,
            "rain_fall": range(20),
            "desc": "Articles about computer science \
                and technology from Ari Birnbaum.",
            "avatar": Profile.objects.first().logo,
            "resume_url": Profile.objects.first().resume_url,
            "favicon": Profile.objects.first().favicon,
            "debug": settings.DEBUG,
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
