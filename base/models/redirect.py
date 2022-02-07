from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


class Redirect(models.Model):
    query_param = models.CharField(
        help_text="The query param to match on.",
        db_index=True,
        verbose_name="Query Param",
        max_length=200,
    )
    redirect_url = models.URLField(
        help_text="Where to redirect this query to.",
        verbose_name="Redirect Url",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Redirect(query_param='{self.query_param}')>"

    def __str__(self):
        return repr(self)

    def redirect(self) -> HttpResponseRedirect:
        return redirect(self.redirect_url)
