import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from utils.general_model import GeneralModel

User = get_user_model()


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}/post/', filename)


class Tag(GeneralModel):
    creator = models.ForeignKey(
        User,
        verbose_name=_("Creator"),
        on_delete=models.CASCADE,
        related_name='Tags'
    )
    name = models.CharField(
        verbose_name=_("Name"),
        unique=True,
        max_length=128,
    )

    def __str__(self):
        return f'{self.creator} {self.name}'
