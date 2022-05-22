from django.contrib import admin

from base.models import Redirect


@admin.register(Redirect)
class AdminRedirect(admin.ModelAdmin):
    list_display = (
        "query_param",
        "redirect_url",
        "times_used",
        "last_modified_at",
        "created_at",
    )
    list_filter = ("last_modified_at", "created_at")
    readonly_fields = ("times_used", "last_modified_at", "created_at")
