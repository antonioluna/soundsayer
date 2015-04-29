#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import default_app, get, post, template, request, static_file,\
response
import requests
from requests_oauthlib import OAuth1, OAuth1Session

scrobble = requests.get('http://ws.audioscrobbler.com/2.0/?')

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
'geo_obtener_ciudades': 'Geo.getMetros'}