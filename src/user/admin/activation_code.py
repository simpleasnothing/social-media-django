from django.contrib import admin


class ActivationCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'used', 'type']
    list_editable = ['type']
    list_filter = ['type', 'used', 'user']
