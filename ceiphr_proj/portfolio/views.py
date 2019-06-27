import os
from django.views.generic import TemplateView
from django.core.cache import cache

from .models import Profile
from .services import get_repos


class GetProjects(TemplateView):
    template_name = "portfolio/projects.html"

    def get_context_data(self, *args, **kwargs):
        cache_key = 'repo_stats'
        cache_time = 1800  # time to live in seconds
        result = cache.get(cache_key)
        if not result:
            result = get_repos()
            cache.set(cache_key, result, cache_time)

        context = {
            "projects": result,
            "is_feed": True,
            "title": "My Projects",
            "desc": "Personal side projects pertaining to computer \
                science and technology from Ari Birnbaum.",
            "avatar": Profile.objects.first().logo,
            "resume_url": Profile.objects.first().resume_url,
            "favicon": Profile.objects.first().favicon,
            "debug": os.getenv('DEBUG', default=True),
        }
        return context
