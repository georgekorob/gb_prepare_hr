import os

from .base import *

# runserver --settings=djproject.settings.prod
DEBUG = False
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ['SECRET_KEY']
