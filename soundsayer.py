#-*- encoding: Utf-8 -*-

#Importamos librerias

from bottle import default_app, get, post, template, request, static_file,\
response, run, route
from bottle_session import SessionPlugin
import requests
from requests_oauthlib import OAuth1, OAuth1Session
import json
import random
import crypt


sesion = SessionPlugin(cookie_lifetime=600)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


#------------------------------------------------------------------------------
#Parte fija local
#------------------------------------------------------------------------------


#Función que encripta texto
def encriptar(cont):
    sal = ""
    for x in range(8):
        sal = sal + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8",
            "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
            "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
            "Z"])
    return crypt.crypt(cont, "$6$" + sal)


#Función que comprueba si una contraseña es válida
def comprobar_login(salt, palabra, archivosh):
    for z in archivosh:
        if crypt.crypt(palabra, salt) == z[1]:
            return True


@route('/')
def index():
    return template('index.tpl')


@route('/comenzar')
def comenzar():
    return template('comenzar.tpl')


@route('/registro')
def registro():
    return template('registro.tpl')


#Intendando hacer request a plantilla de registro

@route('/registro')
def reg():
    reg_header = template('reg_header.tpl').encode('utf-8')
    reg_footer = template('reg_footer.tpl').encode('utf-8')
    return reg_header + '''

<!-- ##########################GENERADO POR BOTTLE######################### -->
    <p>

        <form name="login" action="completar_registro" method="POST" \
accept-charset="utf-8">

            <ul>
                <li><label>Dr. Correo</label>

                <input type="email" name="usermail" \
placeholder="nombre@email.com" required></li>

                <li><label>Password</label>

                <input type="password" name="password" \
placeholder="Contraseña" required></li>

                <li>

                <input type="submit" value="Registrarse" class="button"></li>
            </ul>
        </form>
    </p>

<!-- ##########################GENERADO POR BOTTLE######################### -->
    ''' + reg_footer


@route('/completar_registro', method='POST')
def do_login():
    usermail = request.forms.get('usermail')
    password = request.forms.get('password')
    print usermail
    print password
    #if check_login(usermail, password):
        #return "<p>Your login information was correct.</p>"
    #else:
        #return "<p>Login failed.</p>"


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
