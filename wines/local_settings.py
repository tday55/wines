DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wine',
        'USER': 'wine',
        'PASSWORD': 'wine',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-crhcw-s&cmaf%dcq347s=w38v()auor_i7#()gdgcsb@*8*1(j'

#from django.core.management.utils import get_random_secret_key

#SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

