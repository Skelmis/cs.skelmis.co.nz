from django.contrib import admin

from base.models import Redirect


@admin.register(Redirect)
class AdminRedirect(admin.ModelAdmin):
    list_display = (
        "query_param",
        "times_used",
        "times_embedded_in_discord",
        "requires_authentication",
        "last_modified_at",
        "created_at",
    )
    list_filter = ("last_modified_at", "created_at", "requires_authentication")
    readonly_fields = (
        "times_used",
        "times_embedded_in_discord",
        "last_modified_at",
        "created_at",
    )
