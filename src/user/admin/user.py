from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = ['id', 'email', 'email_verified']
    list_editable = ['email_verified']
    list_filter = ['email_verified']
