from __future__ import absolute_import

from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

SECRET_TOKEN = "4ffaqwqweqwe675f3a4e1127250fccb6fbbac59a41"
