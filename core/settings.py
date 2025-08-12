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
    # unfold admin apps
    "unfold",
    "unfold.contrib.import_export",
    "import_export",
    "unfold.contrib.filters",
    
    
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
    "job_scrap"
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
        "DIRS": [BASE_DIR / "portfolio_app" / "templates"],
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
    "SHOW_BACK_BUTTON": False,
    "SITE_ICON": {
        "light": lambda request: static("img/logo_2.png"),
        "dark": lambda request: static("img/logo_2.png"),
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
              {
                "title": _("Job Hunting"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Local Jobs"),
                        "icon": "work",
                        "link": reverse_lazy("admin:job_scrap_local_changelist"),
                    },
                    {
                        "title": _("International Jobs"),
                        "icon": "enterprise",
                        "link": reverse_lazy("admin:job_scrap_international_changelist"),
                    },
                ],
            },
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
            "50": "248 250 252",  # slate-50 (lighter for modern feel)
            "100": "241 245 249",  # slate-100
            "200": "226 232 240",  # slate-200
            "300": "203 213 225",  # slate-300
            "400": "148 163 184",  # slate-400
            "500": "100 116 139",  # slate-500
            "600": "71 85 105",  # slate-600
            "700": "51 65 85",  # slate-700
            "800": "30 41 59",  # slate-800
            "900": "15 23 42",  # slate-900
            "950": "2 6 23",  # slate-950 (darker)
        },
        "primary": {
            "50": "#fff7ed",  # orange-50
            "100": "#ffedd5",  # orange-100
            "200": "#fed7aa",  # orange-200
            "300": "#fdba74",  # orange-300
            "400": "#fb923c",  # orange-400
            "500": "#f97316",  # orange-500 (primary brand color)
            "600": "#ea580c",  # orange-600
            "700": "#c2410c",  # orange-700
            "800": "#9a3412",  # orange-800
            "900": "#7c2d12",  # orange-900
            "950": "#431407",  # extra dark orange
        },
        "secondary": {
            "50": "#f0f9ff",  # blue-50
            "100": "#e0f2fe",  # blue-100
            "200": "#bae6fd",  # blue-200
            "300": "#7dd3fc",  # blue-300
            "400": "#38bdf8",  # blue-400
            "500": "#0ea5e9",  # blue-500 (secondary accent)
            "600": "#0284c7",  # blue-600
            "700": "#0369a1",  # blue-700
            "800": "#075985",  # blue-800
            "900": "#0c4a6e",  # blue-900
            "950": "#082f49",  # extra dark blue
        },
        "tertiary": {
            "50": "#f8fafc",  # cool gray-50
            "100": "#f1f5f9",  # cool gray-100
            "200": "#e2e8f0",  # cool gray-200
            "300": "#cbd5e1",  # cool gray-300
            "400": "#94a3b8",  # cool gray-400
            "500": "#64748b",  # cool gray-500
            "600": "#475569",  # cool gray-600
            "700": "#334155",  # cool gray-700
            "800": "#1e293b",  # cool gray-800
            "900": "#0f172a",  # cool gray-900
            "950": "#020617",  # near-black
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # slate-500
            "subtle-dark": "var(--color-base-400)",  # slate-400
            "default-light": "var(--color-base-700)",  # slate-700
            "default-dark": "var(--color-base-200)",  # slate-200
            "important-light": "var(--color-base-900)",  # slate-900
            "important-dark": "var(--color-base-50)",  # slate-50
        },
        # "sidebar-selected": "#f97316",  # orange-500 for selected states
    },
    "STYLES": [
        # lambda request: static("css/style.css"),
        lambda request: static("css/admin.css"),
    ],
}


# tailwind settings
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = r"C:\Program Files (x86)\nodejs\npm.cmd"
