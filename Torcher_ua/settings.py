import os
from pathlib import Path
from django.contrib.messages import constants as messages
from secret_key.keys import secret_key, api_key, my_email

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts.apps.AccountsConfig',
    'home_page.apps.HomePageConfig',
    'product.apps.ProductConfig',
    'contacts_page.apps.ContactsPageConfig',
    'news_letter_form.apps.NewsLetterFormConfig',
    'manager.apps.ManagerConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    'about_as.apps.AboutAsConfig',
    'send_email.apps.SendEmailConfig',
    'unsubscribe.apps.UnsubscribeConfig',
    'coupons.apps.CouponsConfig',

    'captcha',
    'six',
    'django_filters',
    'sendgrid',
    'header',
    'footer',
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

ROOT_URLCONF = 'Torcher_ua.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'Torcher_ua.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# user
AUTH_USER_MODEL = 'accounts.CustomUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CART_SESSION_ID = 'cart'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = api_key
EMAIL_USE_TLS = True
RECIPIENTS_EMAIL = [my_email]
DEFAULT_FROM_EMAIL = my_email

PASSWORD_RESET_TIMEOUT = 14400
