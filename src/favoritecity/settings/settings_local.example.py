from django.conf import settings

from favoritecity.settings.database import connect_database


ALLOWED_HOSTS = ["*"]

DATABASES = connect_database(project_path=settings.PROJECT_PATH)

LANGUAGE_CODE = 'ru'

# Toolbar
# DEBUG_TOOLBAR_PATCH_SETTINGS = True
settings.INSTALLED_APPS += ["debug_toolbar"]
settings.MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = [
    "127.0.0.1",
]
