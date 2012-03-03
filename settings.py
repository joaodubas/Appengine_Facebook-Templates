# -*- coding: utf-8 -*-
"""Main configuration file for the application, containing the credentials for
the facebook app.

To obtain the application credentials visit the url:

    https://graph.facebook.com/oauth/access_token

Pass to this url a querystring with the following parameters:

    clicent_id=APP_ID&client_secret=APP_SECRET&grant_type=client_credentials

"""
import os

ADMIN_LIST = ['1', '2']

APP_NAME = u'App Name'
APP_DESC = u'App Desc'

FACEBOOK_APP_ID = 'REAL_FB_APP_ID'
FACEBOOK_APP_SECRET = 'REAL_FB_APP_SECRET'
EXTERNAL_HREF = 'APP_URL'  # WITHOUT trailing slash
FACEBOOK_CANVAS_NAME = 'REAL_FB_CANVAS_NAME'
FACEBOOK_PERMS = ['email', 'publish_stream']

if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    FACEBOOK_APP_ID = 'DEV_FB_APP_ID'
    FACEBOOK_APP_SECRET = 'DEV_FB_APP_SECRET'
    EXTERNAL_HREF = 'DEV_APP_URL'
    FACEBOOK_CANVAS_NAME = 'DEV_FB_CANVAS_NAME-stop-dev'
    FACEBOOK_PERMS = ['email', 'publish_stream']