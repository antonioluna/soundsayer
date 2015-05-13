#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import get, post, template, request, static_file,\
response, run, route
import requests
from requests_oauthlib import OAuth1, OAuth1Session
import json
import random
import crypt


#Ruta estatica
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


#------------------------------------------------------------------------------
#Parte fija local
#------------------------------------------------------------------------------


@route('/')
def index():
    return template('index.tpl')


@route('/comenzar')
def comenzar():
    return template('comenzar.tpl')


@route('/gustos', method='POST')
def do_login():
    username = request.forms.get('username')
    lista_ciudades = []
    lista_ciudades_ord = ''
    contador = 0

    #Parámetros para la API
    para_ciudades = {'method': metodos['geo_obtener_ciudades'], "country": '',
'api_key': api_key, 'format': 'json'}
    para_ciudades['country'] = "spain"
    ciudades = (requests.get(scrobble, params=para_ciudades).text)\
    .encode('utf-8')

    #Convertimos el texto a JSON para tratarlo
    json_c = json.loads(ciudades)

    for x in json_c['metros']['metro']:

        lista_ciudades.append(x['name'])

    lista_ciudades.sort()

    for z in lista_ciudades:
        contador = contador + 1
        lista_ciudades_ord = lista_ciudades_ord + ('<option value="'
        + z + '">' + z + '</option>\n')

    lista_def = '<select name="Ciudad">' + lista_ciudades_ord + '</select>\n'

    cabecera = template('gus_header.tpl', nombre=username)
    pie = template('gus_footer')
    return cabecera + lista_def + pie


@route('/envio_form', method='POST')
def resultados():
    cantautor = request.forms.get('cantautor')
    Grupo = request.forms.get('Grupo')
    Cancion1 = request.forms.get('Cancion1')
    Cancion2 = request.forms.get('Cancion2')
    Cancion3 = request.forms.get('Cancion3')
    Cancion4 = request.forms.get('Cancion4')
    Cancion5 = request.forms.get('Cancion5')
    ciudad = request.forms.get('Ciudad')
    lista = [cantautor, Grupo, Cancion1, Cancion2, Cancion3, Cancion4,
         Cancion5, ciudad]
    return lista


#@route('/pruebas')
#def pruebas():
    #return 'jaja'


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
'geo_obtener_ciudades': 'geo.getMetros',

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


#DEMOSTRACION DE USO DE UNA PETICION GET CON REQUESTS

album_args = {'method': metodos['artista_buscar'], 'artist': '',
'api_key': api_key, 'format': 'json', 'limit': '1'}

album_args['artist'] = 'the prodigy'

r = requests.get(scrobble, params=album_args)

variable = json.loads(r.text)

#print type(variable["results"]['artistmatches']['artist'])


#------------------------------------------------------------------------------
#Parte fija local
#------------------------------------------------------------------------------
run(host='localhost', port=8080)
