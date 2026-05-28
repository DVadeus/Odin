from pathlib import Path

import environ

# Configuración común

# =========================
# Paths
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# =========================
# Environment
# =========================

env = environ.Env()

environ.Env.read_env(BASE_DIR / ".env")


# =========================
# Core
# =========================

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = []


# =========================
# Applications
# =========================

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "storages",
]

LOCAL_APPS = [
    "apps.core",
    "apps.users",
    "apps.accounting",
    "apps.auditing",
    "apps.crm",
    "apps.integrations",
    "apps.inventory",
    "apps.production",
    "apps.purchasing",
    "apps.sales",
]

INSTALLED_APPS = (
    DJANGO_APPS
    + THIRD_PARTY_APPS
    + LOCAL_APPS
)


# =========================
# Middleware
# =========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================
# URLs / WSGI
# =========================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


# =========================
# Templates
# =========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================
# Database
# =========================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}


# =========================
# Cache Redis
# =========================

REDIS_URL = env(
    "REDIS_URL",
    default="redis://redis:6379"
)


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{REDIS_URL}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
        
    }
}


# =========================
# MinIO / S3 Storage
# =========================

AWS_ACCESS_KEY_ID = env("MINIO_ACCESS_KEY")

AWS_SECRET_ACCESS_KEY = env("MINIO_SECRET_KEY")

AWS_STORAGE_BUCKET_NAME = env("MINIO_BUCKET_NAME")

AWS_S3_ENDPOINT_URL = env("MINIO_ENDPOINT")

AWS_S3_REGION_NAME = "us-east-1"

AWS_S3_ADDRESSING_STYLE = "path"

AWS_QUERYSTRING_AUTH = False

AWS_DEFAULT_ACL = None

# =========================
# Django Storage
# =========================

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },

    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# =========================
# Celery Async
# =========================

CELERY_BROKER_URL = f"{REDIS_URL}/0"

CELERY_RESULT_BACKEND = f"{REDIS_URL}/0"

# =========================
# Password validation
# =========================

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


# =========================
# Internationalization
# =========================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =========================
# Static / Media
# =========================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

# Fallback local
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# Default PK
# =========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# Users
# =========================

AUTH_USER_MODEL = "users.User"