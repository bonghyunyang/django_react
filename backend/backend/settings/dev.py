from .common import *

INSTALLED_APPS += [
    'debug_toolbar',
] # 맨 마지막에 넣기

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE # 맨 앞에 넣기

INTERNAL_IPS = ['127.0.0.1']