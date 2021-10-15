import os
import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext as _

from utils.base_errors import BaseErrors
from utils import GeneralModel


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}', filename)


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, GeneralModel):
    username = models.CharField(
        unique=True,
        verbose_name=_('Username'),
        max_length=128,
        null=True,
        blank=True
    )
    cover = models.ImageField(
        verbose_name=_('Cover'),
        upload_to=get_file_path,
        max_length=128,
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email'),
        max_length=256,
    )
    main_image = models.CharField(
        verbose_name=_('Main Image'),
        max_length=1024,
        null=True,
        blank=True,
        unique=True
    )
    email_verified = models.BooleanField(
        verbose_name=_('Email Verified'),
        default=False
    )
    staff = models.BooleanField(
        verbose_name=_('Staff'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Admin'),
        default=False
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )
    follow = models.ManyToManyField(
        'user.User',
        verbose_name=_('Follow'),
    )
    follower_count = models.PositiveIntegerField(
        verbose_name=_('Total Follower'),
        default=0,
    )
    following_count = models.PositiveIntegerField(
        verbose_name=_('Total Following'),
        default=0,
    )
    post_count = models.PositiveIntegerField(
        verbose_name=_('Total post'),
        default=0,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
