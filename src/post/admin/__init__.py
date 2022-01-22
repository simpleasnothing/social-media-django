from django.contrib import admin

from post.admin.comment import CommentAdmin
from post.admin.post import PostAdmin
from post.models import (
    Post as PostModel,
    Comment as CommentModel
)

admin.site.register(PostModel, PostAdmin)
admin.site.register(CommentModel, CommentAdmin)
