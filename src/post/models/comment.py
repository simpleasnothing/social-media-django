from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from utils import GeneralModel

User = get_user_model()


class Comment(GeneralModel):
    user = models.ForeignKey(
        User,
        verbose_name=_('Author'),
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        'post.Post',
        verbose_name=_('Post'),
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name=_('Text'),
    )
    parent = models.ForeignKey(
        'post.Comment',
        verbose_name=_('Parent'),
        related_name='replies',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user} {self.text[:10]}'
