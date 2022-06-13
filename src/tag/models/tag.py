from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from utils import GeneralModel

User = get_user_model()


class Tag(GeneralModel):
    creator = models.ForeignKey(
        User,
        verbose_name=_('Creator'),
        on_delete=models.SET_NULL,
        related_name='tags',
        null=True
    )
    name = models.CharField(
        verbose_name=_('Name'),
        unique=True,
        max_length=128,
    )

    def __str__(self):
        return f'{self.creator} {self.name}'
