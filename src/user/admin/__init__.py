from django.contrib import admin

from user.admin.user import UserAdmin
from user.models import (
        User as UserModel
)

admin.site.register(UserModel, UserAdmin)