#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import default_app, get, post, template, request, static_file,\
response
import requests
from requests_oauthlib import OAuth1, OAuth1Session