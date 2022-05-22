from django.http import HttpRequest
from django.shortcuts import render

from base.models import Redirect


def index_view(request: HttpRequest):
    query_param = request.GET.get("q", False)
    if query_param:
        try:
            return Redirect.objects.get(query_param=query_param).redirect()
        except Redirect.DoesNotExist:
            pass

    context = {'all_routes': []}
    for redirect in Redirect.objects.all():
        context["all_routes"].append(redirect.query_param)

    return render(request, "base/index.html", context=context)
