from django.contrib import admin


class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']
