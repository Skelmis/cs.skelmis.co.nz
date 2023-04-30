from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.shortcuts import render

from base.models import Redirect


def index_view(request: HttpRequest):
    query_param = request.GET.get("q", False)  # type: ignore
    if query_param:
        try:
            redirect = Redirect.objects.get(query_param=query_param)
            if redirect.requires_authentication and not request.user.is_authenticated:
                raise PermissionDenied

            if "Discordbot" in request.headers.get("User-Agent"):
                # Provide OG meta tags
                redirect.times_embedded_in_discord += 1
                redirect.save()

                return render(
                    request,
                    "base/og.html",
                    context={
                        "url": redirect.redirect_url,
                        "meta_color": redirect.meta_color,
                        "meta_title": redirect.meta_title,
                        "meta_description": redirect.meta_description,
                    },
                )

            return redirect.redirect()
        except Redirect.DoesNotExist:
            pass

    context = {"all_routes": [], "auth_routes": []}
    for redirect in Redirect.objects.all():
        if redirect.requires_authentication:
            context["auth_routes"].append(redirect.query_param)
        else:
            context["all_routes"].append(redirect.query_param)

    context["all_routes"] = sorted(context["all_routes"])
    context["auth_routes"] = sorted(context["auth_routes"])

    return render(request, "base/index.html", context=context)
