from favoritecity.settings.database import connect_database
from django.conf import settings


ALLOWED_HOSTS = ["*"]

DATABASES = connect_database(project_path=settings.PROJECT_PATH)

LANGUAGE_CODE = 'ru'
