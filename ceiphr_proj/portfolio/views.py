import os
from django.views.generic import TemplateView
from django.core.cache import cache
from django.shortcuts import render
from django.template import RequestContext

from sentry_sdk import capture_message, last_event_id

from .models import Profile
from .services import get_repos


def page_not_found_view(request, exception, template_name="error-prompt.html"):
    context = {
        "title": "404",
        "desc": "404 — Page Not Found",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    capture_message(exception, level="error")
    return render(request, "error-prompt.html", context, status=404)


def error_view(request, template_name="error-prompt.html"):
    context = {
        "title": "500",
        "desc": "500 — Internal Error",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    capture_message("Internal Error!", level="error")
    return render(request, "error-prompt.html", context, status=500)


def permission_denied_view(request, exception, template_name="error-prompt.html"):
    context = {
        "title": "403",
        "desc": "403 — Permission Denied",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    capture_message(exception, level="error")
    return render(request, "error-prompt.html", context, status=403)


def bad_request_view(request, exception, template_name="error-prompt.html"):
    context = {
        "title": "400",
        "desc": "400 — Bad Request",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    capture_message(exception, level="error")
    return render(request, "error-prompt.html", context, status=400)


"""
Cloudflare Error Pages

These pages are used for Cloudflare's custom error pages. These will be
disabled once the pages are published on Cloudflare.
"""


def banned_ip_view(request, template_name="prompt.html"):
    context = {
        "title": "Access denied",
        "desc": "Sorry, you have been banned.",
        "message": "You cannot access ceiphr.com using the IP address (::CLIENT_IP::).",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


def waf_view(request, template_name="prompt.html"):
    context = {
        "title": "Attention Required!",
        "desc": "Sorry, you have been blocked.",
        "message": "You cannot access ceiphr.com.",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


def error500_view(request, template_name="prompt.html"):
    context = {
        "title": "500",
        "desc": "500 — Internal Error",
        "message": "::CLOUDFLARE_ERROR_500S_BOX::",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


def waf_challenge_view(request, template_name="prompt.html"):
    context = {
        "title": "Attention Required!",
        "desc": "Please complete the security check to access ceiphr.com.",
        "message": "::CAPTCHA_BOX::",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


def error1000_view(request, template_name="prompt.html"):
    context = {
        "title": "1000",
        "desc": "1000 — DNS Resolution Error",
        "message": "::CLOUDFLARE_ERROR_1000S_BOX::",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


def security_challenge_view(request, template_name="prompt.html"):
    context = {
        "title": "Attention Required!",
        "desc": "Please complete the security check to access ceiphr.com.",
        "message": "::CAPTCHA_BOX::",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


def attack_challenge_view(request, template_name="prompt.html"):
    context = {
        "title": "Just a moment...",
        "desc": "Checking your browser before accessing ceiphr.com.",
        "message": "::IM_UNDER_ATTACK_BOX::",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


def rate_limit_view(request, template_name="prompt.html"):
    context = {
        "title": "You are being rate limited.",
        "desc": "You are being rate limited.",
        "message": "You have been banned temporarily from accessing ceiphr.com.",
        "avatar": Profile.objects.first().logo,
        "resume_url": Profile.objects.first().resume_url,
        "favicon": Profile.objects.first().favicon,
    }
    return render(request, "prompt.html", context)


class GetProjects(TemplateView):
    template_name = "portfolio/projects.html"

    def get_context_data(self, *args, **kwargs):
        cache_key = "repo_stats"
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
            "debug": int(os.getenv("DEBUG", default=1)),
        }
        return context
