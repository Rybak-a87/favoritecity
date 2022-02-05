from favoritecity.settings.env_identifier import *   # import (os, Path) here
from favoritecity.settings.database import connect_database


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.join(PROJECT_PATH, 'src')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "accounts.User"

# new admin panel (migrate dashboard and migrate jet)
ENABLE_JET_ADMIN = True
JET_ADMIN_APPS = [
    # new admin panel (migrate dashboard and migrate jet)
    "jet.dashboard",
    "jet",
] if ENABLE_JET_ADMIN else []

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

OWN_APPS = [
    "favoritecity.accounts",
    "favoritecity.ads"
]

# Application definition
INSTALLED_APPS = [
    *JET_ADMIN_APPS,
    *DJANGO_APPS,
    *OWN_APPS,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'favoritecity.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "favoritecity", "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [TEMPLATE_DIR],
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'favoritecity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = connect_database(project_path=PROJECT_PATH)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, "static_content", "static")
# STATIC_DIR = os.path.join(BASE_DIR, "favoritecity", "static")
# STATICFILES_DIRS = (STATIC_DIR,)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "static_content", "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TODO need fixed, this not correct
if DEBUG:
    from favoritecity.settings.settings_local import *
