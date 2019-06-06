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
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap
from django_otp.admin import OTPAdminSite

from .sitemaps import BlogSitemap, StaticViewSitemap
from .feeds import RssSiteNewsFeed, AtomSiteNewsFeed

from blog.views import GetArticle, GetLargeFeed, GetFeed, handler404, handler500
from portfolio.views import GetProjects

import ceiphr.settings.env_config as env_config
from django.conf import settings

# Django 404 and 500 error catcher
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'

# Static URL redirects
favicon_view = RedirectView.as_view(url='/img/favicon.ico', permanent=True)
robots_view = RedirectView.as_view(url='/robots.txt', permanent=True)
humans_view = RedirectView.as_view(url='/humans.txt', permanent=True)
keybase_view = RedirectView.as_view(url='/keybase.txt', permanent=True)

# Sitemaps
sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('favicon.ico', favicon_view),
    path('robots.txt', robots_view),
    path('humans.txt', humans_view),
    path('keybase.txt', keybase_view),

    path('', GetLargeFeed.as_view(template_name="index.html"), name="FrontPage"),

    path('blog/', GetFeed.as_view(template_name="blog.html"), name="Blog"),
    path('blog/?tag=<tag>', GetFeed.as_view(template_name="blog.html")),
    path('blog/<slug>/', GetArticle.as_view(template_name="article.html")),

    path('projects/', GetProjects.as_view(template_name="projects.html"), name="Projects"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('rss.xml', RssSiteNewsFeed()),
    path('rss20.xml', RssSiteNewsFeed()),
    path('atom.xml', AtomSiteNewsFeed()),
]

if settings.DEBUG:
    urlpatterns += [path('admin', admin.site.urls),]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Admin site details
    admin.site.site_header = 'Ceiphr Dashboard: Development'
    admin.site.site_title = 'Ceiphr: Development'

else:
    urlpatterns += [path(env_config.admin_URL+'/admin/', admin.site.urls),]
    admin.site.__class__ = OTPAdminSite

    # Admin site details
    admin.site.site_header = 'Ceiphr Dashboard: Production'
    admin.site.site_title = 'Ceiphr: Production'