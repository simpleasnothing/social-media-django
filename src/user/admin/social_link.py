from django.contrib import admin


class SocialLinkAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['user', 'name', 'url']
    list_editable = ['name']
    list_filter = ['user']
