from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    search_fields = ['caption']
    list_display = ['id', 'caption', 'like_count']
    list_filter = ['user', 'tag']
