from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from utils import GeneralModel
from . import Post

User = get_user_model()


class Comment(GeneralModel):
    user = models.ForeignKey(
        User,
        verbose_name=_('Author'),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    post = models.ForeignKey(
        Post,
        verbose_name=_('Post'),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField(
        verbose_name=_('Text'),
        null=True,
        blank=True,
        default=None,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('Parent'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )
