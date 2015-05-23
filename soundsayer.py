#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import template, request, static_file, run, route
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


def correbusca(lform):

    a_devolver = []

    for art in lform:
        no_modificado = art

        str(art).replace(" ", "").encode('utf-8')

        para_correccion = {'method': metodos['artista_corregir'],
        'artist': art, 'api_key': api_key, 'format': 'json'}
        corregido = requests.get(scrobble, params=para_correccion).json()



        if corregido.has_key('message'):
            return "Existen problemas con el artista %s, por favor cámbielo \
por otro" % (no_modificado)

        if corregido['corrections'] == '\n                ':

            para_buscar = {'method': metodos['artista_buscar'],
        'artist': art, 'api_key': api_key, 'format': 'json', 'limit': '1'}

            buscar = requests.get(scrobble, params=para_buscar).json()
            a_devolver.append(buscar['results']['artistmatches']['artist']
            ['name'])

        if type(corregido['corrections']) is dict:
            correccion_artista = corregido['corrections']
            a_devolver.append(correccion_artista['correction']['artist']
            ['name'])

    return a_devolver

def encuentracanciones(lista):

    #Lista para almacenar los json con los datos de las canciones

    canciones = {}
    lista_total = []

    for x in lista:
        canciones_artista = []
        #Obtenemos las 3 canciones mas escuchadas del cantautor
        para_canta_mejores = {'method': metodos['artista_mejores_canciones'],
        'artist': x, 'api_key': api_key, 'format': 'json', 'limit': '3'}

        mejores_artista = requests.get(scrobble,
        params=para_canta_mejores).json()

        for y in mejores_artista["toptracks"]["track"]:
            datos_canciones = []
            datos_canciones.append(y["name"])

            if y.has_key("image"):
                datos_canciones.append(y["image"][3]['#text'])

            para_youtube = {'q': x + " " + y["name"], 'part': 'id',
            'maxResults': '1', 'key': api_key_yt}

            yt_resp = requests.get(youtube, params=para_youtube)
            if yt_resp.status_code == 200:

                yt_json = yt_resp.json()

                if yt_json["items"][0]["id"].has_key('videoId'):

                    cancion_yt = yt_json["items"][0]["id"]["videoId"]
                    datos_canciones.append(video_url + cancion_yt)
                    lista_total.append(cancion_yt)

            canciones_artista.extend([datos_canciones])

        canciones[x] = canciones_artista

    canciones["reproductor"] = lista_total

    return canciones


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
    ciudades = requests.get(scrobble, params=para_ciudades).json()

    for x in ciudades['metros']['metro']:

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
    formulario = [request.forms.get('artista1'), request.forms.get('artista2'),
        request.forms.get('artista3'), request.forms.get('artista4'),
        request.forms.get('artista5')]

    artistas = correbusca(formulario)
    print artistas

    if type(artistas) is str:
        return artistas


    artistas_totales = []
    for x in artistas:
        para_similares = {'method': metodos['artista_similar'],
        'artist': x, 'api_key': api_key, 'format': 'json', 'limit': '5'}

        similar = requests.get(scrobble, params=para_similares).json()
        artistas_totales.append(x)
        for at in similar["similarartists"]["artist"]:

            if at["name"] not in artistas:
                artistas_totales.append(at["name"])

    json_canciones = encuentracanciones(artistas_totales)

    primer_video = json_canciones["reproductor"][0]
    json_canciones["reproductor"].pop(0)

    video_ids = ""

    for ids in json_canciones["reproductor"]:
        video_ids = video_ids + ids + ","

    video_ids = video_ids + "&"
    video_ids.replace(",&", "&")

    return template("rep_header.tpl", lista_videos=video_ids,
    video1=primer_video)

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