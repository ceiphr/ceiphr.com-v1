from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Profile, Project
from django.conf import settings


class GetProjects(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            "projects": Project.objects.all(),
            "is_feed": True,
            "rain_fall": range(20),
            "title": "My Projects",
            "desc": "Personal side projects pertaining to computer \
                science and technology from Ari Birnbaum.",
            "avatar": Profile.objects.first().logo,
            "resume_url": Profile.objects.first().resume_url,
            "favicon": Profile.objects.first().favicon,
            "debug": settings.DEBUG,
        }
        return context
