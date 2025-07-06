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

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS"), "127.0.0.1", "192.168.22.76"]


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
    BASE_DIR / "theme/static_src/node_modules",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

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
from django.templatetags.static import static


UNFOLD = {
    "SITE_ICON": {
        "light": lambda request: static("img/logo_2.png"),
        "dark": lambda request: static("img/logo_2.png"),
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Authentication"),
                "separator": True,
                "collapsible": True,
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
                "title": _("Visitor's Message"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Inbox"),
                        "icon": "message",
                        "link": reverse_lazy("admin:portfolio_app_inbox_changelist"),
                    },
                ],
            },
            {
                "title": _("Documents"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Resume"),
                        "icon": "work_history",
                        "link": reverse_lazy("admin:portfolio_app_resume_changelist"),
                    },
                ],
            },
            {
                "title": _("Profile"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Profiles"),
                        "icon": "account_circle",
                        "link": reverse_lazy("admin:portfolio_app_profile_changelist"),
                    },
                    {
                        "title": _("Address"),
                        "icon": "location_on",
                        "link": reverse_lazy("admin:portfolio_app_address_changelist"),
                    },
                    {
                        "title": _("Social Links"),
                        "icon": "share",
                        "link": reverse_lazy(
                            "admin:portfolio_app_sociallink_changelist"
                        ),
                    },
                ],
            },
            {
                "title": _("Portfolio Models"),
                "separator": True,
                "collapsible": False,
                "items": [
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
                        "title": _("Certifications"),
                        "icon": "school",
                        "link": reverse_lazy(
                            "admin:portfolio_app_certifications_changelist"
                        ),
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
                        "title": _("Blogs"),
                        "icon": "article",
                        "link": reverse_lazy("admin:portfolio_app_blog_changelist"),
                    },
                    {
                        "title": _("Tags"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:portfolio_app_tag_changelist"),
                    },
                ],
            },
        ],
    },
    "COLORS": {
        "base": {
            "50": "249 250 251",
            "100": "243 244 246",
            "200": "229 231 235",
            "300": "209 213 219",
            "400": "156 163 175",
            "500": "107 114 128",
            "600": "75 85 99",
            "700": "55 65 81",
            "800": "31 41 55",
            "900": "17 24 39",
            "950": "3 7 18",
        },
        "primary": {
            "50": "#FFFBEA",
            "100": "#FFF3C4",
            "200": "#FCE588",
            "300": "#FADB5F",
            "400": "#F7C948",
            "500": "#FFC107",  # Yellow theme
            "600": "#E1A200",
            "700": "#C58C00",
            "800": "#A87900",
            "900": "#855D00",
            "950": "#634300",
        },
        "secondary": {
            "50": "#F4F4F4",
            "100": "#E6E6E6",
            "200": "#CFCFCF",
            "300": "#B8B8B8",
            "400": "#A1A1A1",
            "500": "#8A8A8A",
            "600": "#737373",
            "700": "#5C5C5C",
            "800": "#454545",
            "900": "#2E2E2E",
        },
        "tertiary": {
            "50": "#F5F8FA",
            "100": "#E1E8ED",
            "200": "#CFD9E3",
            "300": "#B3C6D8",
            "400": "#94AFCA",
            "500": "#7395B0",
            "600": "#537090",
            "700": "#3D5470",
            "800": "#263750",
            "900": "#101A30",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",
            "subtle-dark": "var(--color-base-400)",
            "default-light": "var(--color-base-600)",
            "default-dark": "var(--color-base-300)",
            "important-light": "var(--color-base-900)",
            "important-dark": "var(--color-base-100)",
        },
        # "sidebar-selected": "#FFC107",  # Yellow for the selected link
    },
    "STYLES": [
        # lambda request: static("css/style.css"),
        lambda request: static("css/admin.css"),
    ],
    "THEME": "dark",
}


# tailwind settings
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = r"C:\Program Files (x86)\nodejs\npm.cmd"
