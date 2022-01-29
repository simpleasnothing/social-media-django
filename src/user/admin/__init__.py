from django.contrib import admin

from user.admin.activation_code import ActivationCodeAdmin
from user.admin.profile_image import ProfileImageAdmin
from user.admin.social_link import SocialLinkAdmin
from user.admin.user import UserAdmin

from user.models import (
    ActivationCode as ActivationCodeModel,
    ProfileImage as ProfileImageModel,
    SocialLink as SocialLinkModel,
    User as UserModel,
)

admin.site.register(ActivationCodeModel, ActivationCodeAdmin)
admin.site.register(ProfileImageModel, ProfileImageAdmin)
admin.site.register(SocialLinkModel, SocialLinkAdmin)
admin.site.register(UserModel, UserAdmin)
