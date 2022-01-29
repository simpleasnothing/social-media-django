from django.contrib import admin

from tag.admin.tag import TagAdmin
from tag.models import Tag as TagModel

admin.site.register(TagModel, TagAdmin)
