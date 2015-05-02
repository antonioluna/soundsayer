#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import default_app, get, post, template, request, static_file,\
response
import requests
from requests_oauthlib import OAuth1, OAuth1Session
import json


#Url fija de la API
scrobble = 'http://ws.audioscrobbler.com/2.0/?'

#API KEY

api_key = 'a481b1c89d1295cfc279eddb15090338'

#Métodos aceptados por la API

metodos = {'album_informacion': 'Album.getInfo',
'album_comentarios': 'Album.getShouts', 'album_etiquetas': 'Album.getTags',
'album_etiquetas_top': 'Album.getTopTags', 'album_buscar': 'Album.search',

'artista_corregir': 'Artist.getCorrection',
'artista_informacion': 'Artist.getInfo', 'artista_eventos': 'Artist.getEvents',
'artista_similar': 'Artist.getSimilar',
'artista_mejores_discos': 'Artist.getTopAlbums',
'artista_mejores_canciones': 'Artist.getTopTracks',
'artista_': 'Artist.getTags', 'artista_comentarios': 'Artist.getShouts',
'artista_buscar': 'Artist.search',

'geo_eventos': 'Geo.getEvents', 'geo_chart_artista': 'Geo.getMetroArtistChart',
'geo_hype_artista_ciudad': 'Geo.getMetroHypeArtistChart',
'geo_hype_canciones_ciudad': 'Geo.getMetroHypeTrackChart',
'geo_chart_semanal': 'Geo.getMetroWeeklyChartlist',
'geo_artistas_ciudad': 'Geo.getTopArtists',
'geo_canciones_ciudad': 'Geo.getTopTracks',
'geo_obtener_ciudades': 'Geo.getMetros',

'grupo_miembros': 'Group.getMembers',
'grupos_semana_album_chart': 'Group.getWeeklyAlbumChart',
'grupos_semana_artista_chart': 'Group.getWeeklyArtistChart',
'grupos_chart_semanal': 'Group.getWeeklyChartList',
'grupos_chart_semanal_canciones': 'Group.getWeeklyTrackChart',

'etiquetas_informacion': 'Tag.getInfo', 'etiquetas_similar': 'Tag.getSimilar',
'etiquetas_top_albums': 'Tag.getTopAlbums',
'etiquetas_top_artistas': 'Tag.getTopArtists',
'etiquetas_top': 'Tag.getTopTags',
'etiquetas_top_canciones': 'Tag.getTopTracks',
'etiquetas_chart_top_artistas': 'Tag.getWeeklyArtistChart',
'etiquetas_lista_charts_semanal': 'Tag.getWeeklyChartList',
'buscar_tag': 'Tag.search',

'track_enlaces_compra': 'Track.getBuylinks',
'track_correccion': 'Track.getCorrection', 'track_informacion': 'Track.getInfo',
'track_similares': 'Track.getSimilar', 'track_tags': 'Track.getTags',
'track_buscar': 'Track.search'}




artista_args = {}
geo_args = {}
grupos_args = {}
etiquetas_args = {}
tracks_args = {}


#DEMOSTRACION DE USO DE UNA PETICION GET CON REQUESTS

album_args = {'method': metodos['artista_buscar'], 'artist': '',
'api_key': api_key, 'format': 'json', 'limit': '1'}

album_args['artist'] = 'the prodigy'
print album_args['artist']

r = requests.get(scrobble, params=album_args)

variable = json.loads(r.text)

print type(variable["results"]['artistmatches']['artist'])
