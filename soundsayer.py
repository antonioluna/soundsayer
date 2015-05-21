#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import template, request, static_file, response, run, route
import requests
from requests_oauthlib import OAuth1, OAuth1Session
import json
import random


#Ruta estatica
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


#------------------------------------------------------------------------------
#Parte fija local
#------------------------------------------------------------------------------


def encuentracanciones(lista):

    #Lista para almacenar los json con los datos de las canciones
    canciones_list = []

    #Recorremos la lista con los datos del formulario
    for x in lista:

        #Obtenemos las 5 canciones mas escuchadas del cantautor
        para_canta_mejores = {'method': metodos['artista_mejores_canciones'],
        'artist': x, 'api_key': api_key, 'format': 'json', 'limit': '3'}

        canciones_list.append(requests.get(scrobble,
        params=para_canta_mejores).text)

    informacion_canciones = {}
    for z in range(len(canciones_list)):
        total_canciones = []
        datos = json.loads(canciones_list[z].encode('utf-8'))
        for y in datos["toptracks"]["track"]:
            total_canciones.append(y["name"])
            informacion_canciones[lista[z]] = total_canciones

    canciones = []
    for cn in lista:
        videos_artista = []
        for lst in informacion_canciones[cn]:

            para_youtube = {'q': lst, 'part': 'id',
            'maxResults': '1', 'key': api_key_yt}

            yt_resp = requests.get(youtube, params=para_youtube)

            if yt_resp.status_code == 200:
                yt_json = yt_resp.json()

                if yt_json["items"][0]["id"].has_key('videoId'):

                    cancion_yt = yt_json["items"][0]["id"]["videoId"]

                    videos_artista.append(video_url + cancion_yt)

                    canciones.append(videos_artista)

    print canciones
    return informacion_canciones


    ################3#########################################################
    #                                                                       #
    #                      Ruta de la página principal                      #
    #                                                                       #
    #########################################################################

@route('/')
def index():
    return template('index.tpl')


    #########################################################################
    #                                                                       #
    #              Personalizamos con el nombre del usuario                 #
    #                                                                       #
    #########################################################################


@route('/comenzar')
def comenzar():
    return template('comenzar.tpl')


    #########################################################################
    #                                                                       #
    #     Ruta con formularios para recoger los gustos del usuario          #
    #                                                                       #
    #########################################################################


@route('/gustos', method='POST')
def do_login():
    username = request.forms.get('username')
    lista_ciudades = []
    lista_ciudades_ord = ''
    contador = 0

    #Parámetros para la API
    para_ciudades = {'method': metodos['geo_obtener_ciudades'],
    "country": 'spain', 'api_key': api_key, 'format': 'json'}
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


    #########################################################################
    #                                                                       #
    #        Procesamiento de los datos introducidos por el usuario         #
    #                                                                       #
    #########################################################################


@route('/envio_form', method='POST')
def resultados():

    #Lista con datos del formulario
    artistas = [request.forms.get('artista1'), request.forms.get('artista2'),
        request.forms.get('artista3'), request.forms.get('artista4'),
        request.forms.get('artista5')]

    text_similares = []
    for x in artistas:
        x.lower()
        para_similares = {'method': metodos['artista_similar'],
        'artist': x, 'api_key': api_key, 'format': 'json', 'limit': '5'}

        text_similares.append(requests.get(scrobble,
        params=para_similares).text.encode('utf-8'))

    artistas_similares = []
    for t in text_similares:
        json_similar = json.loads(t)
        for i in json_similar["similarartists"]["artist"]:
            artistas_similares.append(i["name"].lower())

    for r in artistas_similares:
        if r not in artistas:
            artistas.append(r)

    return encuentracanciones(artistas)

#Url fija de la API
scrobble = 'http://ws.audioscrobbler.com/2.0/?'
youtube = 'https://www.googleapis.com/youtube/v3/search?'

#API KEY

api_key = 'a481b1c89d1295cfc279eddb15090338'
api_key_yt = 'AIzaSyCwleRrkDzTZV964P87EKfva_zTmrAWhYs'

#URL FIJA VIDEOS YOUTUBE

video_url = 'https://www.youtube.com/watch?v='

#Métodos aceptados por la API

metodos = {'album_informacion': 'Album.getInfo',
'album_comentarios': 'Album.getShouts', 'album_etiquetas': 'Album.getTags',
'album_etiquetas_top': 'Album.getTopTags', 'album_buscar': 'Album.search',

'artista_corregir': 'artist.getcorrection',
'artista_informacion': 'artist.getInfo', 'artista_eventos': 'artist.getEvents',
'artista_similar': 'artist.getsimilar',
'artista_mejores_discos': 'artist.getTopAlbums',
'artista_mejores_canciones': 'artist.gettoptracks',
'artista_': 'artist.getTags', 'artista_comentarios': 'artist.getShouts',
'artista_buscar': 'artist.search',

'geo_eventos': 'geo.getEvents', 'geo_chart_artista': 'geo.getmetroartistchart',
'geo_hype_artista_ciudad': 'Geo.getMetroHypeartistChart',
'geo_hype_canciones_ciudad': 'Geo.getMetroHypeTrackChart',
'geo_chart_semanal': 'geo.getmetroweeklychartlist',
'geo_artistas_ciudad': 'Geo.getTopartists',
'geo_canciones_ciudad': 'Geo.gettoptracks',
'geo_obtener_ciudades': 'geo.getMetros',

'grupo_miembros': 'group.getMembers',
'grupos_semana_album_chart': 'group.getWeeklyAlbumChart',
'grupos_semana_artista_chart': 'group.getWeeklyartistChart',
'grupos_chart_semanal': 'group.getWeeklyChartList',
'grupos_chart_semanal_canciones': 'group.getWeeklyTrackChart',

'etiquetas_informacion': 'tag.getInfo', 'etiquetas_similar': 'tag.getSimilar',
'etiquetas_top_albums': 'tag.getTopAlbums',
'etiquetas_top_artistas': 'tag.getTopartists',
'etiquetas_top': 'tag.getToptags',
'etiquetas_top_canciones': 'tag.gettoptracks',
'etiquetas_chart_top_artistas': 'tag.getWeeklyartistChart',
'etiquetas_lista_charts_semanal': 'tag.getWeeklyChartList',
'buscar_tag': 'tag.search',

'track_enlaces_compra': 'Track.getBuylinks',
'track_correccion': 'Track.getCorrection', 'track_informacion': 'Track.getInfo',
'track_similares': 'Track.getSimilar', 'track_tags': 'Track.gettags',
'track_buscar': 'track.search',

'chart_canciones': 'chart.gettoptracks'}


#------------------------------------------------------------------------------
#Parte fija local
#------------------------------------------------------------------------------
run(host='localhost', port=8080)