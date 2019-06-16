from django.views.generic import TemplateView
from django.conf import settings

from .models import Profile, Project


class GetProjects(TemplateView):
    template_name = "portfolio/projects.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            "projects": Project.objects.all(),
            "is_feed": True,
            "title": "My Projects",
            "desc": "Personal side projects pertaining to computer \
                science and technology from Ari Birnbaum.",
            "avatar": Profile.objects.first().logo,
            "resume_url": Profile.objects.first().resume_url,
            "favicon": Profile.objects.first().favicon,
            "debug": settings.DEBUG,
        }
        return context
