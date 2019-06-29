"""ceiphr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django_otp.admin import OTPAdminSite

from .settings.base import MEDIA_URL, MEDIA_ROOT
from .sitemaps import BlogSitemap, StaticViewSitemap
from .feeds import RssSiteNewsFeed, AtomSiteNewsFeed

from blog.views import GetArticle, GetLargeFeed, GetFeed
from portfolio.views import *

# Error Pages
handler404 = 'portfolio.views.page_not_found_view'
handler500 = 'portfolio.views.error_view'
handler403 = 'portfolio.views.permission_denied_view'
handler400 = 'portfolio.views.bad_request_view'

# Sitemaps
sitemaps = {"static": StaticViewSitemap, "blog": BlogSitemap}

urlpatterns = [

    # RSS/Atom Feeds
    path("rss.xml", RssSiteNewsFeed()),
    path("rss20.xml", RssSiteNewsFeed()),
    path("atom.xml", AtomSiteNewsFeed()),

    # Website Overview URL
    path("",
         GetLargeFeed.as_view(template_name="index.html"),
         name="FrontPage"),

    # Blog URLs
    path(
        "blog/",
        GetFeed.as_view(template_name="blog/blog.html"),
        name="Blog"),

    path(
        "blog/?tag=<tag>",
        GetFeed.as_view(template_name="blog/blog.html")),

    path(
        "blog/<slug>/",
        GetArticle.as_view(template_name="blog/article.html")),

    # Portfolio URLs
    path(
        "projects/",
        GetProjects.as_view(template_name="portfolio/projects.html"),
        name="Projects"),

    # SEO Sitemap URL
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if int(os.environ.get('CF', default=1)):
    # Cloudflare Error Pages
    urlpatterns += [
        path("cf/banned-ip/", banned_ip_view),
        path("cf/rate-limit/", rate_limit_view),
        path("cf/500/", error500_view),
        path("cf/1000/", error1000_view),
        path("cf/waf/", waf_view),
        path("cf/waf-challenge/", waf_challenge_view),
        path("cf/attack-challenge/", attack_challenge_view),
        path("cf/always-online/", always_online_view),
    ]

if int(os.environ.get('DEBUG', default=1)):
    urlpatterns += [path("admin/", admin.site.urls)]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

    # Admin site details
    admin.site.site_header = "Ceiphr Dashboard: Development"
    admin.site.site_title = "Ceiphr: Development"

else:
    urlpatterns += [path(os.environ.get('ADMIN_URL', default="cp") + "/admin/", admin.site.urls)]
    admin.site.__class__ = OTPAdminSite

    # Admin site details
    admin.site.site_header = "Ceiphr Dashboard: Production"
    admin.site.site_title = "Ceiphr: Production"
