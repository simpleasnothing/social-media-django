import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from utils import GeneralModel

User = get_user_model()


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}/post/', filename)


class Post(GeneralModel):
    user = models.ForeignKey(
        User,
        verbose_name=_('Author'),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    caption = models.TextField(
        verbose_name=_('Caption'),
    )
    file = models.ImageField(
        verbose_name=_('Media'),
        upload_to=get_file_path,
        max_length=128,
        null=True,
        blank=True
    )
    tag = models.ManyToManyField(
        'tag.Tag',
        verbose_name=_('Tag')
    )
    like = models.ManyToManyField(
        User,
        verbose_name=_('Like'),
        related_name="likers"
    )
    feed = models.ManyToManyField(
        User,
        verbose_name=_('Feed')
    )
    reshare = models.ForeignKey(
        'post.Post',
        verbose_name=_('Feed'),
        on_delete=models.CASCADE,
        related_name='reshares',
        null=True,
        blank=True,
        default=None
    )
    reshare_count = models.PositiveIntegerField(
        verbose_name=_('Total Reshare'),
        default=0,
    )
    comment_count = models.PositiveIntegerField(
        verbose_name=_('Total Comment'),
        default=0,
    )
    like_count = models.PositiveIntegerField(
        verbose_name=_('Total Like'),
        default=0,
    )

    def __str__(self):
        return f'{self.user} {self.caption[:10]}'
