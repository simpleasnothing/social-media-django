from rest_framework.versioning import URLPathVersioning


class BaseVersioning(URLPathVersioning):
    default_version = 'v1'
    allowed_versions = ['v1']

