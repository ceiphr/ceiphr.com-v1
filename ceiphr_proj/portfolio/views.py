import os
from django.views.generic import TemplateView

from .models import Profile
from .services import get_repos


class GetProjects(TemplateView):
    template_name = "portfolio/projects.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            "projects": get_repos(),
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
