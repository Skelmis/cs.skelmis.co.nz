from colorfield.fields import ColorField
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
    times_used = models.PositiveIntegerField(
        default=0, help_text="How many times this redirect has been used."
    )
    times_embedded_in_discord = models.PositiveIntegerField(
        default=0,
        help_text="How many times discord has requested this URL for embedding on the platform.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    requires_authentication = models.BooleanField(
        default=False, help_text="Does this entry require auth to view?"
    )
    meta_title = models.CharField(
        max_length=55, blank=True, null=True, help_text="Text for the og:title tag"
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        help_text="Text for the og:description tag",
    )
    meta_color = ColorField(default="#808080", help_text="Color for the og:color tag")

    def __repr__(self):
        return f"<Redirect(query_param='{self.query_param}')>"

    def __str__(self):
        return repr(self)

    def redirect(self) -> HttpResponseRedirect:
        self.times_used += 1
        self.save()
        return redirect(self.redirect_url)
