from django.http import HttpRequest, HttpResponse

from base.models import Redirect


def index_view(request: HttpRequest):
    return HttpResponse("Hi")
    query_param = request.GET.get("q", "default_redirect")

    try:
        return Redirect.objects.get(query_param=query_param).redirect()
    except Redirect.DoesNotExist:
        return Redirect.objects.get(query_param="default_redirect").redirect()
