from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.urls import reverse

from blog.models import Article

class RssSiteNewsFeed(Feed):
    title = "Ceiphr"
    author_name = "Ari Birnbaum"
    author_email = 'contact@ceiphr.com'
    feed_url = "/blog"
    link = "/blog"
    description = "Articles about computer science and technology from Ari Birnbaum."
    feed_copyright = 'Copyright (c) 2016 - 2019, Ari Birnbaum (Ceiphr). All Rights Reserved.'

    def items(self):
        return Article.objects.exclude(public=False).order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return item.get_absolute_url() 

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description