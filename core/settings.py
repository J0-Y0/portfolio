import os

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9pc_3$=hb&*^k&z7di)rgprn6mbtc1)(dl6q!a=#3xn($cav3u"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]


# Application definitions

INSTALLED_APPS = [
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fontawesomefree",
    "portfolio_app",
    "tailwind",
    "theme",
    # "django_browser_reload",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# Add these lines to your settings.py
MEDIA_URL = "/media/"
MEDIA_ROOT = (
    BASE_DIR / "media"
)  # This will create a 'media' directory in your project root

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


UNFOLD = {
    "SIDEBAR": {
        "show_search": False,  # Disable search in applications and model names
        "show_all_applications": False,  # Disable dropdown for all apps/models
        "navigation": [
            {
                "title": _("Authentication and Authorization"),
                "separator": True,  # Adds a top border
                "collapsible": True,  # Makes the group collapsible
                "items": [
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                ],
            },
            {
                "title": _("Portfolio Models"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Address"),
                        "icon": "location_on",
                        "link": reverse_lazy("admin:portfolio_app_address_changelist"),
                    },
                    {
                        "title": _("Blogs"),
                        "icon": "article",
                        "link": reverse_lazy("admin:portfolio_app_blog_changelist"),
                    },
                    {
                        "title": _("Certifications"),
                        "icon": "school",
                        "link": reverse_lazy(
                            "admin:portfolio_app_certifications_changelist"
                        ),
                    },
                    {
                        "title": _("Educations"),
                        "icon": "menu_book",
                        "link": reverse_lazy(
                            "admin:portfolio_app_education_changelist"
                        ),
                    },
                    {
                        "title": _("Experiences"),
                        "icon": "work",
                        "link": reverse_lazy(
                            "admin:portfolio_app_experience_changelist"
                        ),
                    },
                    {
                        "title": _("Profiles"),
                        "icon": "account_circle",
                        "link": reverse_lazy("admin:portfolio_app_profile_changelist"),
                    },
                    {
                        "title": _("Projects"),
                        "icon": "build",
                        "link": reverse_lazy("admin:portfolio_app_project_changelist"),
                    },
                    {
                        "title": _("Skills"),
                        "icon": "psychology",
                        "link": reverse_lazy("admin:portfolio_app_skill_changelist"),
                    },
                    {
                        "title": _("Social Links"),
                        "icon": "share",
                        "link": reverse_lazy(
                            "admin:portfolio_app_sociallink_changelist"
                        ),
                    },
                    {
                        "title": _("Tags"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:portfolio_app_tag_changelist"),
                    },
                ],
            },
        ],
    }
}
# tailwind settings
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
