
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from utils.general_model import GeneralModel


User = get_user_model()


class ActivationCode(GeneralModel):

    TYPE_CHOICES = (
        ("REGISTER", "REGISTER"),
        ("FORGET", "FORGET"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Activation Code"),
    )
    type = models.CharField(
        max_length=128,
        choices=TYPE_CHOICES,
        verbose_name=_("Type"),
    )
    code = models.CharField(
        max_length=32,
        verbose_name=_("Code"),
    )
    retry = models.PositiveSmallIntegerField(
        verbose_name=_("Retry"),
        default=0,
    )
    used = models.BooleanField(
        default=False,
        verbose_name=_("Used"),
    )

    class Meta:
        verbose_name = _("ActivationCode")
        verbose_name_plural = _("ActivationCodes")

    def __str__(self):
        return f"{self.user.username}"
