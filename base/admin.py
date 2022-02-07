from django.contrib import admin

from base.models import Redirect


@admin.register(Redirect)
class AdminRedirect(admin.ModelAdmin):
    list_display = ("query_param", "redirect_url", "last_modified_at", "created_at")
    list_filter = ("last_modified_at", "created_at")
    readonly_fields = ("last_modified_at", "created_at")
