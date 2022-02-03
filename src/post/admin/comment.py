from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['text']
    list_display = ['id', 'post', 'text']
    list_filter = ['user', 'post']
