from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'creator']
    list_filter = ['creator']
