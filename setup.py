#-*- encoding: Utf-8 -*-

from bottle import default_app, get, post, template, request, static_file,\
response
import requests
from requests_oauthlib import OAuth1, OAuth1Session

with open("consumer.key", "r") as com_key:
    CONSUMER_KEY = com_key.read()

with open("consumer.scrt", "r") as com_scrt:
    CONSUMER_SECRET = com_scrt.read()

REQUEST_TOKEN_URL = 'https://api.discogs.com/oauth/request_token'
AUTHENTICATE_URL = 'https://www.discogs.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://api.discogs.com/oauth/access_token'
