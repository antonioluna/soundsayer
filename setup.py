#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import default_app, get, post, template, request, static_file,\
response
import requests
from requests_oauthlib import OAuth1, OAuth1Session

scrobble = requests.get('http://ws.audioscrobbler.com/2.0/?')
metodos = {'album_informacion': 'Album.getInfo',
'album_gritos': 'Album.getShouts', 'album_etiquetas': 'Album.getTags',
'album_etiquetas_top': 'Album.getTopTags', 'album_buscar': 'Album.search'}