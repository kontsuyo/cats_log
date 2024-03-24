from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "my",
        "USER": "my",
        "PASSWORD": "my",
        "HOST": "db",
        "PORT": "3306",
        "OPTION": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

INTERNAL_IPS = ["127.0.0.1"]
