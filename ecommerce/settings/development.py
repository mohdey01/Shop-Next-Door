from .base import *
import django_heroku

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')

#Amazon s3 secret keys

AWS_ACCESS_KEY_ID= config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME= config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_SIGNATURE_VERSION = "s3v4"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Activate Django-Heroku.
django_heroku.settings(locals())
