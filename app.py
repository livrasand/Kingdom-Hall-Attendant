from flask import Flask, render_template, request, redirect, g, url_for, jsonify, session, flash, send_file
import sqlite3
import datetime 
from datetime import timedelta
import requests
from bs4 import BeautifulSoup
import json
from flask_mail import Mail, Message
import secrets
import os
import logging
import shutil
from werkzeug.exceptions import HTTPException
from babel.dates import format_date
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'es'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'locales'

app.secret_key = '14b9856a0a051c5e80e072f4de6dfe306f913c3ea5c946f1'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'noresponder.kha@gmail.com'
app.config['MAIL_PASSWORD'] = 'sdlj izlj wpix ipsn'
app.config['MAIL_DEFAULT_SENDER'] = ('Join KHA', 'noresponder.kha@gmail.com')

mail = Mail(app)

babel = Babel(app)

def get_locale():
    return session.get('language')  # Valor por defecto

# Inicializa Babel con la función de selección de idioma
babel.init_app(app, locale_selector=get_locale)

# Configuración de SQLite
DATABASE = 'cavea.db'

def get_db():
    if not hasattr(g, 'bd'):
        g.bd = sqlite3.connect(DATABASE)
        g.bd.row_factory = sqlite3.Row
        logging.debug(f"Conectado a la base de datos principal: {DATABASE}")
    return g.bd

def get_user_db():
    user_db_name = session.get('user_db')
    if not user_db_name:
        logging.error("No se encontró la base de datos del usuario en la sesión.")
        return None
    
    if not hasattr(g, 'bd'):
        g.bd = sqlite3.connect(user_db_name)
        g.bd.row_factory = sqlite3.Row
        logging.debug(f"Conectado a la base de datos del usuario: {user_db_name}")
    return g.bd

@app.before_request
def before_request():
    if 'user_db' in session:
        g.bd = get_user_db()
    else:
        g.bd = get_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'bd'):
        g.bd.close()

def get_last_login(user_id):
    # Crear una conexión directa a cavea.db
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT last_login FROM emptor WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def update_last_login(user_id):
    # Crear una conexión directa a cavea.db
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    if cursor:
        try:
            logging.debug("Ejecutando la consulta para actualizar last_login.")
            cursor.execute("UPDATE emptor SET last_login = ? WHERE id = ?", (datetime.datetime.now(), user_id))
            conn.commit()  # Cambiado de cursor.commit() a conn.commit()
            logging.debug("El last_login se ha actualizado correctamente.")
        except Exception as e:
            logging.error(f"Error al actualizar last_login: {e}")
        finally:
            conn.close()  # Asegurarse de cerrar la conexión
    else:
        logging.error("No se pudo obtener la base de datos principal para actualizar el último inicio de sesión.")

@app.route('/')
def welcome():
    return render_template('welcome.html')

#@app.errorhandler(Exception)
#def handle_exception(e):
#    code = 404
#    if isinstance(e, HTTPException):
#        code = e.code
#    return render_template('404.html'), code

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/helloworld')
def helloworld():
    return 'Hello World!!'

@app.route('/login-desktop-client')
def login_desktop():
    return render_template('login-desktop-client.html')

@app.route('/home')
def index():
    if 'user_id' not in session:
        flash("No se puede acceder a la base de datos del usuario.")
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    apply_golden_style = session.get('user_ge', 'no') == 'yes'

    last_login = get_last_login(user_id)
    if last_login and datetime.datetime.now() - datetime.datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f') > timedelta(hours=1):
        flash("La sesión ha expirado. Por favor, inicia sesión nuevamente.")
        return redirect(url_for('login'))
    
    try:
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM configuracion")
        user_data = cursor.fetchall()

        cursor.execute("SELECT idioma FROM configuracion")
        result = cursor.fetchone()
        session['language'] = result['idioma']
        print(f"Idioma actual: {session['language']}")

    except Exception as e:
        flash(f"Ha ocurrido un error interno con la base de datos: {str(e)}.")
        app.logger.error(f"Error al consultar la base de datos: {str(e)}")
        return redirect(url_for('login'))

    return render_template('index.html', user_data=user_data, apply_golden_style=apply_golden_style)

@app.route('/congregacion.html')
def option_one():
    if not hasattr(g, 'bd'):
        flash("No se puede acceder a la base de datos del usuario.")
        return redirect(url_for('login'))
    
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM congregacion WHERE id = ?", (1,))
    congregation_data = cursor.fetchone()

    return render_template('congregacion.html', congregation=congregation_data)

@app.route('/guardar_congregacion', methods=['POST'])
def guardar_congregacion():
    if request.method == 'POST':
        nombre_congregacion = request.form['nombre_congregacion']
        numero = request.form['numero']
        hora_inicio_semana = request.form['hora_inicio_semana']
        hora_inicio_fin_semana = request.form['hora_inicio_fin_semana']
        
        # Aquí agregamos strip() para eliminar espacios en blanco adicionales
        direccion_salon = request.form['direccion_salon'].strip()
        print(f"Dirección del salón sin espacios: '{direccion_salon}'")  # Depuración
        
        superintendente_circuito = request.form['superintendente_circuito']
        telefono = request.form['telefono']
        circuito = request.form['circuito']

        opcion_semana = request.form.get('options')
        opcion_fin_semana = request.form.get('optionstwo')

        cursor = g.bd.cursor()
        cursor.execute("SELECT * FROM congregacion WHERE nombre_congregacion = ?", (nombre_congregacion,))
        existing_congregation = cursor.fetchone()

        if existing_congregation:
            g.bd.execute("UPDATE congregacion SET numero=?, hora_inicio_semana=?, hora_inicio_fin_semana=?, direccion_salon=?, superintendente_circuito=?, telefono=?, circuito=?, opcion_semana=?, opcion_fin_semana=? WHERE nombre_congregacion=?",
                          (numero, hora_inicio_semana, hora_inicio_fin_semana, direccion_salon, superintendente_circuito, telefono, circuito, opcion_semana, opcion_fin_semana, nombre_congregacion))
        else:
            g.bd.execute("INSERT INTO congregacion (nombre_congregacion, numero, hora_inicio_semana, hora_inicio_fin_semana, direccion_salon, superintendente_circuito, telefono, circuito, opcion_semana, opcion_fin_semana) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (nombre_congregacion, numero, hora_inicio_semana, hora_inicio_fin_semana, direccion_salon, superintendente_circuito, telefono, circuito, opcion_semana, opcion_fin_semana))

        g.bd.commit()

        return redirect('/congregacion.html')

@app.route('/publicadores.html')
def publicadores():
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM publicadores")
    publicadores = cursor.fetchall()
    return render_template('publicadores.html', publicador_list=publicadores)

@app.route('/nuevo_publicador')
def nuevo_publicador():
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM familias")
    familia_existente = cursor.fetchall()
    cursor.execute("SELECT * FROM familias")
    familias = cursor.fetchall()
    cursor.execute("SELECT * FROM grupos_predicacion")
    grupos_predicacion = cursor.fetchall()
    return render_template('detalle-publicador.html', publicador=None, familia_existente=familia_existente, grupos_predicacion=grupos_predicacion, familias=familias)


@app.route('/mostrar_publicador/<int:id>', methods=['GET'])
def mostrar_publicador(id):
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM publicadores WHERE id = ?", (id,))
    publicador = cursor.fetchone()

    apellidos = publicador[2]

    cursor.execute("SELECT * FROM grupos_predicacion")
    grupos_predicacion = cursor.fetchall()

    cursor.execute("SELECT * FROM familias WHERE apellidos_familia = ?", (apellidos,))
    familia_existente = cursor.fetchone() is not None

    cursor.execute("SELECT * FROM familias")
    familias = cursor.fetchall()

    return render_template('detalle-publicador.html', publicador=publicador, familia_existente=familia_existente, familias=familias, grupos_predicacion=grupos_predicacion)

@app.route('/guardar_publicador', methods=['POST'])
def guardar_publicador():
    if request.method == 'POST':
        id = request.form['id']  
        nombres = request.form['nombres'].strip()
        apellidos = request.form['apellidos'].strip()
        genero = request.form['genero']
        cabeza_de_familia = 'cabeza_de_familia' in request.form 
        familia = request.form['familia'] 
        tipo_miembro_familia = request.form['relacion']
        fecha_nacimiento = request.form['fecha_nacimiento']
        grupo_predicacion = request.form['grupo_predicacion']
        direccion = request.form['direccion']
        correo_electronico = request.form['correo_electronico']
        celular = request.form['celular']
        telefono = request.form['telefono']
        bautizado = 'bautizado_checkbox' in request.form
        fecha_bautizo = request.form['fecha_bautizo_input'] if 'fecha_bautizo_input' in request.form else None
        recibe_atalaya = 'recibe_atalaya' in request.form
        recibe_guia_actividades = 'recibe_guia_actividades' in request.form
        no_bautizado = 'no_bautizado' in request.form
        temporal = 'temporal' in request.form
        ungido = 'ungido' in request.form
        nino = 'nino' in request.form
        readmitido = 'readmitido' in request.form
        irregular = 'irregular' in request.form
        invidente = 'invidente' in request.form
        abuso_sexual = 'abuso_sexual' in request.form
        divorciado = 'divorciado' in request.form
        viudo = 'viudo' in request.form
        sordo = 'sordo' in request.form
        enfermo = 'enfermo' in request.form
        voluntario_ldc = 'voluntario_ldc' in request.form
        voluntario_epc = 'voluntario_epc' in request.form
        llaves_salon = 'llaves_salon' in request.form
        utiliza_kha = 'utiliza_kha' in request.form
        censurado = 'censurado' in request.form
        inactivo = 'inactivo' in request.form
        expulsado = 'expulsado' in request.form
        fallecido = 'fallecido' in request.form
        encarcelado = 'encarcelado' in request.form
        separado = 'separado' in request.form
        nombramientos = request.form['nombramientos']
        fecha_inicio_nombrado = request.form['fecha_inicio_nombrado']
        privilegios_servicio = request.form['privilegios_servicio']
        fecha_inicio = request.form['fecha_inicio']
        numero_precursor = request.form['numero_precursor']
        temporario = 'temporario' in request.form
        enfermizo = 'enfermizo' in request.form
        fecha_ultima_escuela = request.form['fecha_ultima_escuela']
        checkbox_coordinador_cuerpo_ancianos = 'checkbox-coordinador-cuerpo-ancianos' in request.form
        checkbox_secretario = 'checkbox-secretario' in request.form
        checkbox_superintendente_servicio = 'checkbox-superintendente-servicio' in request.form
        checkbox_siervo_acomodadores = 'checkbox-siervo-acomodadores' in request.form
        checkbox_coordinador_audio_video = 'checkbox-coordinador-audio-video' in request.form
        checkbox_siervo_literatura = 'checkbox-siervo-literatura' in request.form
        checkbox_coordinador_mantenimiento = 'checkbox-coordinador-mantenimiento' in request.form
        checkbox_coordinador_mantenimiento_jardin = 'checkbox-coordinador-mantenimiento-jardin' in request.form
        checkbox_comite_mantenimiento_salon_reino = 'checkbox-comite-mantenimiento-salon-reino' in request.form
        checkbox_consejero_sala_auxiliar = 'checkbox-consejero-sala-auxiliar' in request.form
        checkbox_consejero_auxiliar = 'checkbox-consejero-auxiliar' in request.form
        checkbox_voluntario_temporal_betel = 'checkbox-voluntario-temporal-betel' in request.form
        checkbox_betelita_cercanias = 'checkbox-betelita-cercanias' in request.form
        checkbox_voluntario_remoto_betel = 'checkbox-voluntario-remoto-betel' in request.form
        checkbox_comite_enlace_hospitalario = 'checkbox-comite-enlace-hospitalario' in request.form
        checkbox_conductor_estudio_atalaya = 'checkbox-conductor-estudio-atalaya' in request.form
        checkbox_coordinador_discursos_publicos = 'checkbox-coordinador-discursos-publicos' in request.form
        checkbox_ayudante_coordinador_discursos_publicos = 'checkbox-ayudante-coordinador-discursos-publicos' in request.form
        checkbox_siervo_informes = 'checkbox-siervo-informes' in request.form
        checkbox_siervo_cuentas = 'checkbox-siervo-cuentas' in request.form
        checkbox_siervo_territorios = 'checkbox-siervo-territorios' in request.form
        checkbox_coordinador_limpieza = 'checkbox-coordinador-limpieza' in request.form
        checkbox_superintendente_reunion_vida_ministerio_cristianos = 'checkbox-superintendente-reunion-vida-ministerio-cristianos' in request.form
        checkbox_coordinador_predicacion_publica = 'checkbox-coordinador-predicacion-publica' in request.form
        checkbox_superintendente_grupo = 'checkbox-superintendente-grupo' in request.form
        checkbox_siervo_grupo = 'checkbox-siervo-grupo' in request.form
        checkbox_auxiliar_grupo = 'checkbox-auxiliar-grupo' in request.form
        checkbox_betelita = 'checkbox-betelita' in request.form
        checkbox_voluntario_construccion = 'checkbox-voluntario-construccion' in request.form
        checkbox_siervo_construccion = 'checkbox-siervo-construccion' in request.form
        checkbox_presidente = 'checkbox-presidente' in request.form
        checkbox_oracion = 'checkbox-oracion' in request.form
        checkbox_discurso_10_mins = 'checkbox-discurso-10-mins' in request.form
        checkbox_busquemos_perlas_escondidas = 'checkbox-busquemos-perlas-escondidas' in request.form
        checkbox_lectura_biblia = 'checkbox-lectura-biblia' in request.form
        checkbox_analisis = 'checkbox-analisis' in request.form
        checkbox_empiece_conversaciones = 'checkbox-empiece-conversaciones' in request.form
        checkbox_haga_revisitas = 'checkbox-haga-revisitas' in request.form
        checkbox_haga_discipulos = 'checkbox-haga-discipulos' in request.form
        checkbox_no_utilizar_sala_principal = 'checkbox-no-utilizar-sala-principal' in request.form
        checkbox_explique_sus_creencias = 'checkbox-explique-sus-creencias' in request.form
        checkbox_ayudante = 'checkbox-ayudante' in request.form
        checkbox_discurso = 'checkbox-discurso' in request.form
        checkbox_utilizar_solo_sala_principal = 'checkbox-utilizar-solo-sala-principal' in request.form
        checkbox_intervenciones = 'checkbox-intervenciones' in request.form
        checkbox_estudio_biblico_congregacion = 'checkbox-estudio-biblico-congregacion' in request.form
        checkbox_lector = 'checkbox-lector' in request.form
        checkbox_discursante_publico_saliente = 'checkbox-discursante-publico-saliente' in request.form
        checkbox_discursante_publico_local = 'checkbox-discursante-publico-local' in request.form
        checkbox_presidente_reunion_publica = 'checkbox-presidente-reunion-publica' in request.form
        checkbox_lector_atalaya = 'checkbox-lector-atalaya' in request.form
        checkbox_anfitrion_hospitalidades = 'checkbox-anfitrion-hospitalidades' in request.form
        checkbox_operador_audio = 'checkbox-operador-audio' in request.form
        checkbox_plataforma = 'checkbox-plataforma' in request.form
        checkbox_anfitrion_zoom = 'checkbox-anfitrion-zoom' in request.form
        checkbox_microfonos = 'checkbox-microfonos' in request.form
        checkbox_coanfitrion_zoom = 'checkbox-coanfitrion-zoom' in request.form
        checkbox_acomodador = 'checkbox-acomodador' in request.form
        checkbox_aprobado_predicacion_publica = 'checkbox-aprobado-predicacion-publica' in request.form
        checkbox_dirigir_reuniones_servicio_campo = 'checkbox-dirigir-reuniones-servicio-campo' in request.form
        checkbox_orar_reuniones_servicio_campo = 'checkbox-orar-reuniones-servicio-campo' in request.form
        checkbox_limpieza_semanal_salon_reino = 'checkbox-limpieza-semanal-salon-reino' in request.form
        checkbox_limpieza_despues_reunion = 'checkbox-limpieza-despues-reunion' in request.form
        checkbox_cuidado_jardin = 'checkbox-cuidado-jardin' in request.form
        checkbox_limpieza_mensual_salon_reino = 'checkbox-limpieza-mensual-salon-reino' in request.form
        checkbox_limpieza_trimestral_salon_reino = 'checkbox-limpieza-trimestral-salon-reino' in request.form
        checkbox_cuidado_cesped = 'checkbox-cuidado-cesped' in request.form

        cabeza_de_familia = 1 if cabeza_de_familia else 0
        bautizado = 1 if bautizado else 0
        recibe_atalaya = 1 if recibe_atalaya else 0
        recibe_guia_actividades = 1 if recibe_guia_actividades else 0
        no_bautizado = 1 if no_bautizado else 0
        temporal = 1 if temporal else 0
        ungido = 1 if ungido else 0
        nino = 1 if nino else 0
        readmitido = 1 if readmitido else 0
        irregular = 1 if irregular else 0
        invidente = 1 if invidente else 0
        abuso_sexual = 1 if abuso_sexual else 0
        divorciado = 1 if divorciado else 0
        viudo = 1 if viudo else 0
        sordo = 1 if sordo else 0
        enfermo = 1 if enfermo else 0
        voluntario_ldc = 1 if voluntario_ldc else 0
        voluntario_epc = 1 if voluntario_epc else 0
        llaves_salon = 1 if llaves_salon else 0
        utiliza_kha = 1 if utiliza_kha else 0
        censurado = 1 if censurado else 0
        inactivo = 1 if inactivo else 0
        expulsado = 1 if expulsado else 0
        fallecido = 1 if fallecido else 0
        encarcelado = 1 if encarcelado else 0
        separado = 1 if separado else 0        
        temporario = 1 if temporario else 0
        enfermizo = 1 if enfermizo else 0
        checkbox_coordinador_cuerpo_ancianos = 1 if checkbox_coordinador_cuerpo_ancianos else 0
        checkbox_secretario = 1 if checkbox_secretario else 0
        checkbox_superintendente_servicio = 1 if checkbox_superintendente_servicio else 0
        checkbox_siervo_acomodadores = 1 if checkbox_siervo_acomodadores else 0
        checkbox_coordinador_audio_video = 1 if checkbox_coordinador_audio_video else 0
        checkbox_siervo_literatura = 1 if checkbox_siervo_literatura else 0
        checkbox_coordinador_mantenimiento = 1 if checkbox_coordinador_mantenimiento else 0
        checkbox_coordinador_mantenimiento_jardin = 1 if checkbox_coordinador_mantenimiento_jardin else 0
        checkbox_comite_mantenimiento_salon_reino = 1 if checkbox_comite_mantenimiento_salon_reino else 0
        checkbox_consejero_sala_auxiliar = 1 if checkbox_consejero_sala_auxiliar else 0
        checkbox_consejero_auxiliar = 1 if checkbox_consejero_auxiliar else 0
        checkbox_voluntario_temporal_betel = 1 if checkbox_voluntario_temporal_betel else 0
        checkbox_betelita_cercanias = 1 if checkbox_betelita_cercanias else 0
        checkbox_voluntario_remoto_betel = 1 if checkbox_voluntario_remoto_betel else 0
        checkbox_comite_enlace_hospitalario = 1 if checkbox_comite_enlace_hospitalario else 0
        checkbox_conductor_estudio_atalaya = 1 if checkbox_conductor_estudio_atalaya else 0
        checkbox_coordinador_discursos_publicos = 1 if checkbox_coordinador_discursos_publicos else 0
        checkbox_ayudante_coordinador_discursos_publicos = 1 if checkbox_ayudante_coordinador_discursos_publicos else 0
        checkbox_siervo_informes = 1 if checkbox_siervo_informes else 0
        checkbox_siervo_cuentas = 1 if checkbox_siervo_cuentas else 0
        checkbox_siervo_territorios = 1 if checkbox_siervo_territorios else 0
        checkbox_coordinador_limpieza = 1 if checkbox_coordinador_limpieza else 0
        checkbox_superintendente_reunion_vida_ministerio_cristianos = 1 if checkbox_superintendente_reunion_vida_ministerio_cristianos else 0
        checkbox_coordinador_predicacion_publica = 1 if checkbox_coordinador_predicacion_publica else 0
        checkbox_superintendente_grupo = 1 if checkbox_superintendente_grupo else 0
        checkbox_siervo_grupo = 1 if checkbox_siervo_grupo else 0
        checkbox_auxiliar_grupo = 1 if checkbox_auxiliar_grupo else 0
        checkbox_betelita = 1 if checkbox_betelita else 0
        checkbox_voluntario_construccion = 1 if checkbox_voluntario_construccion else 0
        checkbox_siervo_construccion = 1 if checkbox_siervo_construccion else 0
        checkbox_presidente = 1 if checkbox_presidente else 0
        checkbox_oracion = 1 if checkbox_oracion else 0
        checkbox_discurso_10_mins = 1 if checkbox_discurso_10_mins else 0
        checkbox_busquemos_perlas_escondidas = 1 if checkbox_busquemos_perlas_escondidas else 0
        checkbox_lectura_biblia = 1 if checkbox_lectura_biblia else 0
        checkbox_analisis = 1 if checkbox_analisis else 0
        checkbox_empiece_conversaciones = 1 if checkbox_empiece_conversaciones else 0
        checkbox_haga_revisitas = 1 if checkbox_haga_revisitas else 0
        checkbox_haga_discipulos = 1 if checkbox_haga_discipulos else 0
        checkbox_no_utilizar_sala_principal = 1 if checkbox_no_utilizar_sala_principal else 0
        checkbox_explique_sus_creencias = 1 if checkbox_explique_sus_creencias else 0
        checkbox_ayudante = 1 if checkbox_ayudante else 0
        checkbox_discurso = 1 if checkbox_discurso else 0
        checkbox_utilizar_solo_sala_principal = 1 if checkbox_utilizar_solo_sala_principal else 0
        checkbox_intervenciones = 1 if checkbox_intervenciones else 0
        checkbox_estudio_biblico_congregacion = 1 if checkbox_estudio_biblico_congregacion else 0
        checkbox_lector = 1 if checkbox_lector else 0
        checkbox_discursante_publico_saliente = 1 if checkbox_discursante_publico_saliente else 0
        checkbox_discursante_publico_local = 1 if checkbox_discursante_publico_local else 0
        checkbox_presidente_reunion_publica = 1 if checkbox_presidente_reunion_publica else 0
        checkbox_lector_atalaya = 1 if checkbox_lector_atalaya else 0
        checkbox_anfitrion_hospitalidades = 1 if checkbox_anfitrion_hospitalidades else 0
        checkbox_operador_audio = 1 if checkbox_operador_audio else 0
        checkbox_plataforma = 1 if checkbox_plataforma else 0
        checkbox_anfitrion_zoom = 1 if checkbox_anfitrion_zoom else 0
        checkbox_microfonos = 1 if checkbox_microfonos else 0
        checkbox_coanfitrion_zoom = 1 if checkbox_coanfitrion_zoom else 0
        checkbox_acomodador = 1 if checkbox_acomodador else 0
        checkbox_aprobado_predicacion_publica = 1 if checkbox_aprobado_predicacion_publica else 0
        checkbox_dirigir_reuniones_servicio_campo = 1 if checkbox_dirigir_reuniones_servicio_campo else 0
        checkbox_orar_reuniones_servicio_campo = 1 if checkbox_orar_reuniones_servicio_campo else 0
        checkbox_limpieza_semanal_salon_reino = 1 if checkbox_limpieza_semanal_salon_reino else 0
        checkbox_limpieza_despues_reunion = 1 if checkbox_limpieza_despues_reunion else 0
        checkbox_cuidado_jardin = 1 if checkbox_cuidado_jardin else 0
        checkbox_limpieza_mensual_salon_reino = 1 if checkbox_limpieza_mensual_salon_reino else 0
        checkbox_limpieza_trimestral_salon_reino = 1 if checkbox_limpieza_trimestral_salon_reino else 0
        checkbox_cuidado_cesped = 1 if checkbox_cuidado_cesped else 0

        cursor = g.bd.cursor()
        cursor.execute("SELECT * FROM publicadores WHERE nombres = ? AND apellidos = ?", (nombres, apellidos))
        existing_publicador = cursor.fetchone()

        if existing_publicador:
            g.bd.execute("UPDATE publicadores SET nombres=?, apellidos=?, genero=?, cabeza_de_familia=?, familia=?, tipo_miembro_familia=?, fecha_nacimiento=?, grupo_predicacion = ?, direccion=?, correo_electronico=?, celular=?, telefono=?, bautizado=?, fecha_bautizo=?, recibe_atalaya=?, recibe_guia_actividades=?, no_bautizado=?, temporal=?, ungido=?, nino=?, readmitido=?, irregular=?, invidente=?, abuso_sexual=?, divorciado=?, viudo=?, sordo=?, enfermo=?, voluntario_ldc=?, voluntario_epc=?, llaves_salon=?, utiliza_kha=?, censurado=?, inactivo=?, expulsado=?, fallecido=?, encarcelado=?, separado=?, nombramientos=?, fecha_inicio_nombrado=?, privilegios_servicio=?, fecha_inicio=?, numero_precursor=?, temporario=?, enfermizo=?, fecha_ultima_escuela=?, checkbox_coordinador_cuerpo_ancianos=?, checkbox_secretario=?, checkbox_superintendente_servicio=?, checkbox_siervo_acomodadores=?, checkbox_coordinador_audio_video=?, checkbox_siervo_literatura=?, checkbox_coordinador_mantenimiento=?, checkbox_coordinador_mantenimiento_jardin=?, checkbox_comite_mantenimiento_salon_reino=?, checkbox_consejero_sala_auxiliar=?, checkbox_consejero_auxiliar=?, checkbox_voluntario_temporal_betel=?, checkbox_betelita_cercanias=?, checkbox_voluntario_remoto_betel=?, checkbox_comite_enlace_hospitalario=?, checkbox_conductor_estudio_atalaya=?, checkbox_coordinador_discursos_publicos=?, checkbox_ayudante_coordinador_discursos_publicos=?, checkbox_siervo_informes=?, checkbox_siervo_cuentas=?, checkbox_siervo_territorios=?, checkbox_coordinador_limpieza=?, checkbox_superintendente_reunion_vida_ministerio_cristianos=?, checkbox_coordinador_predicacion_publica=?, checkbox_superintendente_grupo=?, checkbox_siervo_grupo=?, checkbox_auxiliar_grupo=?, checkbox_betelita=?, checkbox_voluntario_construccion=?, checkbox_siervo_construccion=?, checkbox_presidente=?, checkbox_oracion=?, checkbox_discurso_10_mins=?, checkbox_busquemos_perlas_escondidas=?, checkbox_lectura_biblia=?, checkbox_analisis=?, checkbox_empiece_conversaciones=?, checkbox_haga_revisitas=?, checkbox_haga_discipulos=?, checkbox_no_utilizar_sala_principal=?, checkbox_explique_sus_creencias=?, checkbox_ayudante=?, checkbox_discurso=?, checkbox_utilizar_solo_sala_principal=?, checkbox_intervenciones=?, checkbox_estudio_biblico_congregacion=?, checkbox_lector=?, checkbox_discursante_publico_saliente=?, checkbox_discursante_publico_local=?, checkbox_presidente_reunion_publica=?, checkbox_lector_atalaya=?, checkbox_anfitrion_hospitalidades=?, checkbox_operador_audio=?, checkbox_plataforma=?, checkbox_anfitrion_zoom=?, checkbox_microfonos=?, checkbox_coanfitrion_zoom=?, checkbox_acomodador=?, checkbox_aprobado_predicacion_publica=?, checkbox_dirigir_reuniones_servicio_campo=?, checkbox_orar_reuniones_servicio_campo=?, checkbox_limpieza_semanal_salon_reino=?, checkbox_limpieza_despues_reunion=?, checkbox_cuidado_jardin=?, checkbox_limpieza_mensual_salon_reino=?, checkbox_limpieza_trimestral_salon_reino=?, checkbox_cuidado_cesped=? WHERE id=?",
                (nombres, apellidos, genero, cabeza_de_familia, familia, tipo_miembro_familia, fecha_nacimiento, grupo_predicacion, direccion, correo_electronico, celular, telefono, bautizado, fecha_bautizo, recibe_atalaya, recibe_guia_actividades, no_bautizado, temporal, ungido, nino, readmitido, irregular, invidente, abuso_sexual, divorciado, viudo, sordo, enfermo, voluntario_ldc, voluntario_epc, llaves_salon, utiliza_kha, censurado, inactivo, expulsado, fallecido, encarcelado, separado, nombramientos, fecha_inicio_nombrado, privilegios_servicio, fecha_inicio, numero_precursor, temporario, enfermizo, fecha_ultima_escuela, checkbox_coordinador_cuerpo_ancianos, checkbox_secretario, checkbox_superintendente_servicio, checkbox_siervo_acomodadores, checkbox_coordinador_audio_video, checkbox_siervo_literatura, checkbox_coordinador_mantenimiento, checkbox_coordinador_mantenimiento_jardin, checkbox_comite_mantenimiento_salon_reino, checkbox_consejero_sala_auxiliar, checkbox_consejero_auxiliar, checkbox_voluntario_temporal_betel, checkbox_betelita_cercanias, checkbox_voluntario_remoto_betel, checkbox_comite_enlace_hospitalario, checkbox_conductor_estudio_atalaya, checkbox_coordinador_discursos_publicos, checkbox_ayudante_coordinador_discursos_publicos, checkbox_siervo_informes, checkbox_siervo_cuentas, checkbox_siervo_territorios, checkbox_coordinador_limpieza, checkbox_superintendente_reunion_vida_ministerio_cristianos, checkbox_coordinador_predicacion_publica, checkbox_superintendente_grupo, checkbox_siervo_grupo, checkbox_auxiliar_grupo, checkbox_betelita, checkbox_voluntario_construccion, checkbox_siervo_construccion, checkbox_presidente, checkbox_oracion, checkbox_discurso_10_mins, checkbox_busquemos_perlas_escondidas, checkbox_lectura_biblia, checkbox_analisis, checkbox_empiece_conversaciones, checkbox_haga_revisitas, checkbox_haga_discipulos, checkbox_no_utilizar_sala_principal, checkbox_explique_sus_creencias, checkbox_ayudante, checkbox_discurso, checkbox_utilizar_solo_sala_principal, checkbox_intervenciones, checkbox_estudio_biblico_congregacion, checkbox_lector, checkbox_discursante_publico_saliente, checkbox_discursante_publico_local, checkbox_presidente_reunion_publica, checkbox_lector_atalaya, checkbox_anfitrion_hospitalidades, checkbox_operador_audio, checkbox_plataforma, checkbox_anfitrion_zoom, checkbox_microfonos, checkbox_coanfitrion_zoom, checkbox_acomodador, checkbox_aprobado_predicacion_publica, checkbox_dirigir_reuniones_servicio_campo, checkbox_orar_reuniones_servicio_campo, checkbox_limpieza_semanal_salon_reino, checkbox_limpieza_despues_reunion, checkbox_cuidado_jardin, checkbox_limpieza_mensual_salon_reino, checkbox_limpieza_trimestral_salon_reino, checkbox_cuidado_cesped, existing_publicador[0]))

            g.bd.commit()
        else:
            g.bd.execute("INSERT INTO publicadores (nombres, apellidos, genero, cabeza_de_familia, familia, tipo_miembro_familia, fecha_nacimiento, grupo_predicacion, direccion, correo_electronico, celular, telefono, bautizado, fecha_bautizo, recibe_atalaya, recibe_guia_actividades, no_bautizado, temporal, ungido, nino, readmitido, irregular, invidente, abuso_sexual, divorciado, viudo, sordo, enfermo, voluntario_ldc, voluntario_epc, llaves_salon, utiliza_kha, censurado, inactivo, expulsado, fallecido, encarcelado, separado, nombramientos, fecha_inicio_nombrado, privilegios_servicio, fecha_inicio, numero_precursor, temporario, enfermizo, fecha_ultima_escuela, checkbox_coordinador_cuerpo_ancianos, checkbox_secretario, checkbox_superintendente_servicio, checkbox_siervo_acomodadores, checkbox_coordinador_audio_video, checkbox_siervo_literatura, checkbox_coordinador_mantenimiento, checkbox_coordinador_mantenimiento_jardin, checkbox_comite_mantenimiento_salon_reino, checkbox_consejero_sala_auxiliar, checkbox_consejero_auxiliar, checkbox_voluntario_temporal_betel, checkbox_betelita_cercanias, checkbox_voluntario_remoto_betel, checkbox_comite_enlace_hospitalario, checkbox_conductor_estudio_atalaya, checkbox_coordinador_discursos_publicos, checkbox_ayudante_coordinador_discursos_publicos, checkbox_siervo_informes, checkbox_siervo_cuentas, checkbox_siervo_territorios, checkbox_coordinador_limpieza, checkbox_superintendente_reunion_vida_ministerio_cristianos, checkbox_coordinador_predicacion_publica, checkbox_superintendente_grupo, checkbox_siervo_grupo, checkbox_auxiliar_grupo, checkbox_betelita, checkbox_voluntario_construccion, checkbox_siervo_construccion, checkbox_presidente, checkbox_oracion, checkbox_discurso_10_mins, checkbox_busquemos_perlas_escondidas, checkbox_lectura_biblia, checkbox_analisis, checkbox_empiece_conversaciones, checkbox_haga_revisitas, checkbox_haga_discipulos, checkbox_no_utilizar_sala_principal, checkbox_explique_sus_creencias, checkbox_ayudante, checkbox_discurso, checkbox_utilizar_solo_sala_principal, checkbox_intervenciones, checkbox_estudio_biblico_congregacion, checkbox_lector, checkbox_discursante_publico_saliente, checkbox_discursante_publico_local, checkbox_presidente_reunion_publica, checkbox_lector_atalaya, checkbox_anfitrion_hospitalidades, checkbox_operador_audio, checkbox_plataforma, checkbox_anfitrion_zoom, checkbox_microfonos, checkbox_coanfitrion_zoom, checkbox_acomodador, checkbox_aprobado_predicacion_publica, checkbox_dirigir_reuniones_servicio_campo, checkbox_orar_reuniones_servicio_campo, checkbox_limpieza_semanal_salon_reino, checkbox_limpieza_despues_reunion, checkbox_cuidado_jardin, checkbox_limpieza_mensual_salon_reino, checkbox_limpieza_trimestral_salon_reino, checkbox_cuidado_cesped) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (nombres, apellidos, genero, cabeza_de_familia, familia, tipo_miembro_familia, fecha_nacimiento, grupo_predicacion, direccion, correo_electronico, celular, telefono, bautizado, fecha_bautizo, recibe_atalaya, recibe_guia_actividades, no_bautizado, temporal, ungido, nino, readmitido, irregular, invidente, abuso_sexual, divorciado, viudo, sordo, enfermo, voluntario_ldc, voluntario_epc, llaves_salon, utiliza_kha, censurado, inactivo, expulsado, fallecido, encarcelado, separado, nombramientos, fecha_inicio_nombrado, privilegios_servicio, fecha_inicio, numero_precursor, temporario, enfermizo, fecha_ultima_escuela, checkbox_coordinador_cuerpo_ancianos, checkbox_secretario, checkbox_superintendente_servicio, checkbox_siervo_acomodadores, checkbox_coordinador_audio_video, checkbox_siervo_literatura, checkbox_coordinador_mantenimiento, checkbox_coordinador_mantenimiento_jardin, checkbox_comite_mantenimiento_salon_reino, checkbox_consejero_sala_auxiliar, checkbox_consejero_auxiliar, checkbox_voluntario_temporal_betel, checkbox_betelita_cercanias, checkbox_voluntario_remoto_betel, checkbox_comite_enlace_hospitalario, checkbox_conductor_estudio_atalaya, checkbox_coordinador_discursos_publicos, checkbox_ayudante_coordinador_discursos_publicos, checkbox_siervo_informes, checkbox_siervo_cuentas, checkbox_siervo_territorios, checkbox_coordinador_limpieza, checkbox_superintendente_reunion_vida_ministerio_cristianos, checkbox_coordinador_predicacion_publica, checkbox_superintendente_grupo, checkbox_siervo_grupo, checkbox_auxiliar_grupo, checkbox_betelita, checkbox_voluntario_construccion, checkbox_siervo_construccion, checkbox_presidente, checkbox_oracion, checkbox_discurso_10_mins, checkbox_busquemos_perlas_escondidas, checkbox_lectura_biblia, checkbox_analisis, checkbox_empiece_conversaciones, checkbox_haga_revisitas, checkbox_haga_discipulos, checkbox_no_utilizar_sala_principal, checkbox_explique_sus_creencias, checkbox_ayudante, checkbox_discurso, checkbox_utilizar_solo_sala_principal, checkbox_intervenciones, checkbox_estudio_biblico_congregacion, checkbox_lector, checkbox_discursante_publico_saliente, checkbox_discursante_publico_local, checkbox_presidente_reunion_publica, checkbox_lector_atalaya, checkbox_anfitrion_hospitalidades, checkbox_operador_audio, checkbox_plataforma, checkbox_anfitrion_zoom, checkbox_microfonos, checkbox_coanfitrion_zoom, checkbox_acomodador, checkbox_aprobado_predicacion_publica, checkbox_dirigir_reuniones_servicio_campo, checkbox_orar_reuniones_servicio_campo, checkbox_limpieza_semanal_salon_reino, checkbox_limpieza_despues_reunion, checkbox_cuidado_jardin, checkbox_limpieza_mensual_salon_reino, checkbox_limpieza_trimestral_salon_reino, checkbox_cuidado_cesped))
        
            g.bd.commit()

            if cabeza_de_familia:
                pass

    return redirect('/publicadores.html')

@app.route('/eliminar_publicador/<int:id>', methods=['GET'])
def eliminar_publicador(id):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM publicadores WHERE id = ?", (id,))
    g.bd.commit()
    return redirect('/publicadores.html')

@app.route('/configuracion.html')
def configuracion():
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM configuracion WHERE id = ?", (1,))
    configuracion_data = cursor.fetchone()

    return render_template('configuracion.html', configuracion=configuracion_data)

@app.route('/guardar_configuracion', methods=['POST'])
def guardar_configuracion():
    if request.method == 'POST':
        id = request.form['id']
        idioma = request.form['idioma']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        user_email = request.form['user_email']
        privilegio = request.form['privilegio']
        pais = request.form['pais']
        congregacion = request.form['congregacion']
        circuito = request.form['circuito']

        session['language'] = idioma

        cursor = g.bd.cursor()

        # Verificar si ya existe una configuración para este usuario
        cursor.execute("SELECT * FROM configuracion WHERE id = ?", (id,))
        existing_config = cursor.fetchone()

        if existing_config:
            # Si ya existe una configuración, actualizarla
            cursor.execute("""
                UPDATE configuracion
                SET nombre = ?, apellidos = ?, user_email = ?, privilegio = ?, pais = ?, congregacion = ?, circuito = ?, idioma = ?
                WHERE id = ?
            """, (nombre, apellidos, user_email, privilegio, pais, congregacion, circuito, idioma, id))
        else:
            # Si no existe una configuración, insertarla
            cursor.execute("""
                INSERT INTO configuracion (nombre, apellidos, user_email, privilegio, pais, congregacion, circuito, idioma)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (nombre, apellidos, user_email, privilegio, pais, congregacion, circuito, idioma))
            
        g.bd.commit()        

    return redirect('/configuracion.html')

@app.route('/grupos-predicacion.html')
def grupos_predicacion():

    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM grupos_predicacion")
    grupos = cursor.fetchall()

    return render_template('/grupos-predicacion.html', grupos=grupos)

@app.route('/nuevo_grupo', methods=['GET'])
def nuevo_grupo():
    cursor = g.bd.cursor()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_siervo_grupo = 1")
    publicadores_siervo = cursor.fetchall()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_auxiliar_grupo = 1")
    publicadores_auxiliar = cursor.fetchall()

    return render_template('detalle-grupo-predicacion.html', grupo=None, publicadores_siervo=publicadores_siervo, publicadores_auxiliar=publicadores_auxiliar)

@app.route('/mostrar_grupo/<int:id>', methods=['GET'])
def mostrar_grupo(id):
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM grupos_predicacion WHERE id = ?", (id,))
    grupo = cursor.fetchone()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_siervo_grupo = 1")
    publicadores_siervo = cursor.fetchall()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_auxiliar_grupo = 1")
    publicadores_auxiliar = cursor.fetchall()

    return render_template('detalle-grupo-predicacion.html', grupo=grupo, publicadores_siervo=publicadores_siervo, publicadores_auxiliar=publicadores_auxiliar)

@app.route('/guardar_grupo', methods=['POST'])
def guardar_grupo():
    if request.method == 'POST':
        nombre_grupo = request.form['nombre_grupo']
        siervo_grupo = request.form['siervo_grupo']
        auxiliar_grupo = request.form['auxiliar_grupo']
        direccion_grupo = request.form['direccion_grupo']
        asignar_hospitalidad = request.form.get('asignar_hospitalidad') == 'on'
        limpieza_salon = request.form.get('limpieza_salon') == 'on'
        reunion_superintendente = request.form.get('reunion_superintendente') == 'on'

        cursor = g.bd.cursor()

        cursor.execute("""
            INSERT INTO grupos_predicacion (nombre_grupo, siervo_grupo, auxiliar_grupo, direccion_grupo, asignar_hospitalidad, limpieza_salon, reunion_superintendente)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre_grupo, siervo_grupo, auxiliar_grupo, direccion_grupo, asignar_hospitalidad, limpieza_salon, reunion_superintendente))

        g.bd.commit() 

    return redirect('/grupos-predicacion.html')

@app.route('/eliminar_grupo/<int:id>', methods=['GET'])
def eliminar_grupo(id):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM grupos_predicacion WHERE id = ?", (id,))
    g.bd.commit()
    return redirect('/grupos-predicacion.html')

@app.route('/crear_familia/<apellidos>', methods=['GET'])
def crear_familia(apellidos):
    if request.method == 'GET':
        cursor = g.bd.cursor()

        cursor.execute("SELECT * FROM familias WHERE apellidos_familia = ?", (apellidos,))
        familia_existente = cursor.fetchone()

        if not familia_existente:
            cursor.execute("INSERT INTO familias (apellidos_familia) VALUES (?)", (apellidos,))
            g.bd.commit()

        return redirect(request.referrer)

@app.route('/oradores.html')
def oradores():
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM oradores")
    oradores = cursor.fetchall()
    cursor.execute("SELECT id, nombres, apellidos FROM publicadores WHERE checkbox_discursante_publico_saliente = 1 OR checkbox_discursante_publico_local = 1")
    publicadores_discursantes = cursor.fetchall()
    return render_template('oradores.html', orador_list=oradores, publicadores_discursantes_list=publicadores_discursantes)

@app.route('/crear_orador', methods=['GET'])
def crear_orador():
  nombres = request.args.get('nombres')
  apellidos = request.args.get('apellidos')

  cursor = g.bd.cursor()
  cursor.execute("SELECT * FROM oradores WHERE nombres = ? AND apellidos = ?", (nombres, apellidos))
  orador_existente = cursor.fetchone()

  if not orador_existente:
    cursor.execute("INSERT INTO oradores (nombres, apellidos) VALUES (?, ?)", (nombres, apellidos))
    g.bd.commit()

  return redirect('/oradores.html')

@app.route('/mostrar_orador/<int:id>', methods=['GET'])
def mostrar_orador(id):
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM oradores WHERE id = ?", (id,))
    orador = cursor.fetchone()
    return render_template('detalle-orador.html', orador=orador)

@app.route('/guardar_orador', methods=['POST'])
def guardar_orador():
    if request.method == 'POST':
        id = request.form['id'] 
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        aprobado_para_salir = request.form.get('aprobado_para_salir') == 'on'
        aprobado_para_salir = 1 if aprobado_para_salir else 0 
        correo_electronico = request.form['correo_electronico']
        celular = request.form['celular']
        telefono = request.form['telefono']
        congregacion = request.form['congregacion']
        
        nombramiento = request.form.get('nombramiento')

        discurso_1 = 'discurso_1' in request.form
        discurso_1 = 1 if discurso_1 else 0

        discurso_2 = 'discurso_2' in request.form
        discurso_2 = 1 if discurso_2 else 0

        discurso_3 = 'discurso_3' in request.form
        discurso_3 = 1 if discurso_3 else 0

        discurso_4 = 'discurso_4' in request.form
        discurso_4 = 1 if discurso_4 else 0

        discurso_5 = 'discurso_5' in request.form
        discurso_5 = 1 if discurso_5 else 0

        discurso_6 = 'discurso_6' in request.form
        discurso_6 = 1 if discurso_6 else 0

        discurso_7 = 'discurso_7' in request.form
        discurso_7 = 1 if discurso_7 else 0

        discurso_8 = 'discurso_8' in request.form
        discurso_8 = 1 if discurso_8 else 0

        discurso_9 = 'discurso_9' in request.form
        discurso_9 = 1 if discurso_9 else 0

        discurso_10 = 'discurso_10' in request.form
        discurso_10 = 1 if discurso_10 else 0

        discurso_11 = 'discurso_11' in request.form
        discurso_11 = 1 if discurso_11 else 0

        discurso_12 = 'discurso_12' in request.form
        discurso_12 = 1 if discurso_12 else 0

        discurso_13 = 'discurso_13' in request.form
        discurso_13 = 1 if discurso_13 else 0

        discurso_14 = 'discurso_14' in request.form
        discurso_14 = 1 if discurso_14 else 0

        discurso_15 = 'discurso_15' in request.form
        discurso_15 = 1 if discurso_15 else 0

        discurso_16 = 'discurso_16' in request.form
        discurso_16 = 1 if discurso_16 else 0

        discurso_17 = 'discurso_17' in request.form
        discurso_17 = 1 if discurso_17 else 0

        discurso_18 = 'discurso_18' in request.form
        discurso_18 = 1 if discurso_18 else 0

        discurso_19 = 'discurso_19' in request.form
        discurso_19 = 1 if discurso_19 else 0

        discurso_20 = 'discurso_20' in request.form
        discurso_20 = 1 if discurso_20 else 0

        discurso_21 = 'discurso_21' in request.form
        discurso_21 = 1 if discurso_21 else 0

        discurso_22 = 'discurso_22' in request.form
        discurso_22 = 1 if discurso_22 else 0

        discurso_23 = 'discurso_23' in request.form
        discurso_23 = 1 if discurso_23 else 0

        discurso_24 = 'discurso_24' in request.form
        discurso_24 = 1 if discurso_24 else 0

        discurso_25 = 'discurso_25' in request.form
        discurso_25 = 1 if discurso_25 else 0

        discurso_26 = 'discurso_26' in request.form
        discurso_26 = 1 if discurso_26 else 0

        discurso_27 = 'discurso_27' in request.form
        discurso_27 = 1 if discurso_27 else 0

        discurso_28 = 'discurso_28' in request.form
        discurso_28 = 1 if discurso_28 else 0

        discurso_29 = 'discurso_29' in request.form
        discurso_29 = 1 if discurso_29 else 0

        discurso_30 = 'discurso_30' in request.form
        discurso_30 = 1 if discurso_30 else 0

        discurso_31 = 'discurso_31' in request.form
        discurso_31 = 1 if discurso_31 else 0

        discurso_32 = 'discurso_32' in request.form
        discurso_32 = 1 if discurso_32 else 0

        discurso_33 = 'discurso_33' in request.form
        discurso_33 = 1 if discurso_33 else 0

        discurso_34 = 'discurso_34' in request.form
        discurso_34 = 1 if discurso_34 else 0

        discurso_35 = 'discurso_35' in request.form
        discurso_35 = 1 if discurso_35 else 0

        discurso_36 = 'discurso_36' in request.form
        discurso_36 = 1 if discurso_36 else 0

        discurso_37 = 'discurso_37' in request.form
        discurso_37 = 1 if discurso_37 else 0

        discurso_38 = 'discurso_38' in request.form
        discurso_38 = 1 if discurso_38 else 0

        discurso_39 = 'discurso_39' in request.form
        discurso_39 = 1 if discurso_39 else 0

        discurso_40 = 'discurso_40' in request.form
        discurso_40 = 1 if discurso_40 else 0

        discurso_41 = 'discurso_41' in request.form
        discurso_41 = 1 if discurso_41 else 0

        discurso_42 = 'discurso_42' in request.form
        discurso_42 = 1 if discurso_42 else 0

        discurso_43 = 'discurso_43' in request.form
        discurso_43 = 1 if discurso_43 else 0

        discurso_44 = 'discurso_44' in request.form
        discurso_44 = 1 if discurso_44 else 0

        discurso_45 = 'discurso_45' in request.form
        discurso_45 = 1 if discurso_45 else 0

        discurso_46 = 'discurso_46' in request.form
        discurso_46 = 1 if discurso_46 else 0

        discurso_47 = 'discurso_47' in request.form
        discurso_47 = 1 if discurso_47 else 0

        discurso_48 = 'discurso_48' in request.form
        discurso_48 = 1 if discurso_48 else 0

        discurso_49 = 'discurso_49' in request.form
        discurso_49 = 1 if discurso_49 else 0

        discurso_50 = 'discurso_50' in request.form
        discurso_50 = 1 if discurso_50 else 0

        discurso_51 = 'discurso_51' in request.form
        discurso_51 = 1 if discurso_51 else 0

        discurso_52 = 'discurso_52' in request.form
        discurso_52 = 1 if discurso_52 else 0

        discurso_53 = 'discurso_53' in request.form
        discurso_53 = 1 if discurso_53 else 0

        discurso_54 = 'discurso_54' in request.form
        discurso_54 = 1 if discurso_54 else 0

        discurso_55 = 'discurso_55' in request.form
        discurso_55 = 1 if discurso_55 else 0

        discurso_56 = 'discurso_56' in request.form
        discurso_56 = 1 if discurso_56 else 0

        discurso_57 = 'discurso_57' in request.form
        discurso_57 = 1 if discurso_57 else 0

        discurso_58 = 'discurso_58' in request.form
        discurso_58 = 1 if discurso_58 else 0

        discurso_59 = 'discurso_59' in request.form
        discurso_59 = 1 if discurso_59 else 0

        discurso_60 = 'discurso_60' in request.form
        discurso_60 = 1 if discurso_60 else 0

        discurso_61 = 'discurso_61' in request.form
        discurso_61 = 1 if discurso_61 else 0

        discurso_62 = 'discurso_62' in request.form
        discurso_62 = 1 if discurso_62 else 0

        discurso_63 = 'discurso_63' in request.form
        discurso_63 = 1 if discurso_63 else 0

        discurso_64 = 'discurso_64' in request.form
        discurso_64 = 1 if discurso_64 else 0

        discurso_65 = 'discurso_65' in request.form
        discurso_65 = 1 if discurso_65 else 0

        discurso_66 = 'discurso_66' in request.form
        discurso_66 = 1 if discurso_66 else 0

        discurso_67 = 'discurso_67' in request.form
        discurso_67 = 1 if discurso_67 else 0

        discurso_68 = 'discurso_68' in request.form
        discurso_68 = 1 if discurso_68 else 0

        discurso_69 = 'discurso_69' in request.form
        discurso_69 = 1 if discurso_69 else 0

        discurso_70 = 'discurso_70' in request.form
        discurso_70 = 1 if discurso_70 else 0

        discurso_71 = 'discurso_71' in request.form
        discurso_71 = 1 if discurso_71 else 0

        discurso_72 = 'discurso_72' in request.form
        discurso_72 = 1 if discurso_72 else 0

        discurso_73 = 'discurso_73' in request.form
        discurso_73 = 1 if discurso_73 else 0

        discurso_74 = 'discurso_74' in request.form
        discurso_74 = 1 if discurso_74 else 0

        discurso_75 = 'discurso_75' in request.form
        discurso_75 = 1 if discurso_75 else 0

        discurso_76 = 'discurso_76' in request.form
        discurso_76 = 1 if discurso_76 else 0

        discurso_77 = 'discurso_77' in request.form
        discurso_77 = 1 if discurso_77 else 0

        discurso_78 = 'discurso_78' in request.form
        discurso_78 = 1 if discurso_78 else 0

        discurso_79 = 'discurso_79' in request.form
        discurso_79 = 1 if discurso_79 else 0

        discurso_80 = 'discurso_80' in request.form
        discurso_80 = 1 if discurso_80 else 0

        discurso_81 = 'discurso_81' in request.form
        discurso_81 = 1 if discurso_81 else 0

        discurso_82 = 'discurso_82' in request.form
        discurso_82 = 1 if discurso_82 else 0

        discurso_83 = 'discurso_83' in request.form
        discurso_83 = 1 if discurso_83 else 0

        discurso_84 = 'discurso_84' in request.form
        discurso_84 = 1 if discurso_84 else 0

        discurso_85 = 'discurso_85' in request.form
        discurso_85 = 1 if discurso_85 else 0

        discurso_86 = 'discurso_86' in request.form
        discurso_86 = 1 if discurso_86 else 0

        discurso_87 = 'discurso_87' in request.form
        discurso_87 = 1 if discurso_87 else 0

        discurso_88 = 'discurso_88' in request.form
        discurso_88 = 1 if discurso_88 else 0

        discurso_89 = 'discurso_89' in request.form
        discurso_89 = 1 if discurso_89 else 0

        discurso_90 = 'discurso_90' in request.form
        discurso_90 = 1 if discurso_90 else 0

        discurso_91 = 'discurso_91' in request.form
        discurso_91 = 1 if discurso_91 else 0

        discurso_92 = 'discurso_92' in request.form
        discurso_92 = 1 if discurso_92 else 0

        discurso_93 = 'discurso_93' in request.form
        discurso_93 = 1 if discurso_93 else 0

        discurso_94 = 'discurso_94' in request.form
        discurso_94 = 1 if discurso_94 else 0

        discurso_95 = 'discurso_95' in request.form
        discurso_95 = 1 if discurso_95 else 0

        discurso_96 = 'discurso_96' in request.form
        discurso_96 = 1 if discurso_96 else 0

        discurso_97 = 'discurso_97' in request.form
        discurso_97 = 1 if discurso_97 else 0

        discurso_98 = 'discurso_98' in request.form
        discurso_98 = 1 if discurso_98 else 0

        discurso_99 = 'discurso_99' in request.form
        discurso_99 = 1 if discurso_99 else 0

        discurso_100 = 'discurso_100' in request.form
        discurso_100 = 1 if discurso_100 else 0

        discurso_101 = 'discurso_101' in request.form
        discurso_101 = 1 if discurso_101 else 0

        discurso_102 = 'discurso_102' in request.form
        discurso_102 = 1 if discurso_102 else 0

        discurso_103 = 'discurso_103' in request.form
        discurso_103 = 1 if discurso_103 else 0

        discurso_104 = 'discurso_104' in request.form
        discurso_104 = 1 if discurso_104 else 0

        discurso_105 = 'discurso_105' in request.form
        discurso_105 = 1 if discurso_105 else 0

        discurso_106 = 'discurso_106' in request.form
        discurso_106 = 1 if discurso_106 else 0

        discurso_107 = 'discurso_107' in request.form
        discurso_107 = 1 if discurso_107 else 0

        discurso_108 = 'discurso_108' in request.form
        discurso_108 = 1 if discurso_108 else 0

        discurso_109 = 'discurso_109' in request.form
        discurso_109 = 1 if discurso_109 else 0

        discurso_110 = 'discurso_110' in request.form
        discurso_110 = 1 if discurso_110 else 0

        discurso_111 = 'discurso_111' in request.form
        discurso_111 = 1 if discurso_111 else 0

        discurso_112 = 'discurso_112' in request.form
        discurso_112 = 1 if discurso_112 else 0

        discurso_113 = 'discurso_113' in request.form
        discurso_113 = 1 if discurso_113 else 0

        discurso_114 = 'discurso_114' in request.form
        discurso_114 = 1 if discurso_114 else 0

        discurso_115 = 'discurso_115' in request.form
        discurso_115 = 1 if discurso_115 else 0

        discurso_116 = 'discurso_116' in request.form
        discurso_116 = 1 if discurso_116 else 0

        discurso_117 = 'discurso_117' in request.form
        discurso_117 = 1 if discurso_117 else 0

        discurso_118 = 'discurso_118' in request.form
        discurso_118 = 1 if discurso_118 else 0

        discurso_119 = 'discurso_119' in request.form
        discurso_119 = 1 if discurso_119 else 0

        discurso_120 = 'discurso_120' in request.form
        discurso_120 = 1 if discurso_120 else 0

        discurso_121 = 'discurso_121' in request.form
        discurso_121 = 1 if discurso_121 else 0

        discurso_122 = 'discurso_122' in request.form
        discurso_122 = 1 if discurso_122 else 0

        discurso_123 = 'discurso_123' in request.form
        discurso_123 = 1 if discurso_123 else 0

        discurso_124 = 'discurso_124' in request.form
        discurso_124 = 1 if discurso_124 else 0

        discurso_125 = 'discurso_125' in request.form
        discurso_125 = 1 if discurso_125 else 0

        discurso_126 = 'discurso_126' in request.form
        discurso_126 = 1 if discurso_126 else 0

        discurso_127 = 'discurso_127' in request.form
        discurso_127 = 1 if discurso_127 else 0

        discurso_128 = 'discurso_128' in request.form
        discurso_128 = 1 if discurso_128 else 0

        discurso_129 = 'discurso_129' in request.form
        discurso_129 = 1 if discurso_129 else 0

        discurso_130 = 'discurso_130' in request.form
        discurso_130 = 1 if discurso_130 else 0

        discurso_131 = 'discurso_131' in request.form
        discurso_131 = 1 if discurso_131 else 0

        discurso_132 = 'discurso_132' in request.form
        discurso_132 = 1 if discurso_132 else 0

        discurso_133 = 'discurso_133' in request.form
        discurso_133 = 1 if discurso_133 else 0

        discurso_134 = 'discurso_134' in request.form
        discurso_134 = 1 if discurso_134 else 0

        discurso_135 = 'discurso_135' in request.form
        discurso_135 = 1 if discurso_135 else 0

        discurso_136 = 'discurso_136' in request.form
        discurso_136 = 1 if discurso_136 else 0

        discurso_137 = 'discurso_137' in request.form
        discurso_137 = 1 if discurso_137 else 0

        discurso_138 = 'discurso_138' in request.form
        discurso_138 = 1 if discurso_138 else 0

        discurso_139 = 'discurso_139' in request.form
        discurso_139 = 1 if discurso_139 else 0

        discurso_140 = 'discurso_140' in request.form
        discurso_140 = 1 if discurso_140 else 0

        discurso_141 = 'discurso_141' in request.form
        discurso_141 = 1 if discurso_141 else 0

        discurso_142 = 'discurso_142' in request.form
        discurso_142 = 1 if discurso_142 else 0

        discurso_143 = 'discurso_143' in request.form
        discurso_143 = 1 if discurso_143 else 0

        discurso_144 = 'discurso_144' in request.form
        discurso_144 = 1 if discurso_144 else 0

        discurso_145 = 'discurso_145' in request.form
        discurso_145 = 1 if discurso_145 else 0

        discurso_146 = 'discurso_146' in request.form
        discurso_146 = 1 if discurso_146 else 0

        discurso_147 = 'discurso_147' in request.form
        discurso_147 = 1 if discurso_147 else 0

        discurso_148 = 'discurso_148' in request.form
        discurso_148 = 1 if discurso_148 else 0

        discurso_149 = 'discurso_149' in request.form
        discurso_149 = 1 if discurso_149 else 0

        discurso_150 = 'discurso_150' in request.form
        discurso_150 = 1 if discurso_150 else 0

        discurso_151 = 'discurso_151' in request.form
        discurso_151 = 1 if discurso_151 else 0

        discurso_152 = 'discurso_152' in request.form
        discurso_152 = 1 if discurso_152 else 0

        discurso_153 = 'discurso_153' in request.form
        discurso_153 = 1 if discurso_153 else 0

        discurso_154 = 'discurso_154' in request.form
        discurso_154 = 1 if discurso_154 else 0

        discurso_155 = 'discurso_155' in request.form
        discurso_155 = 1 if discurso_155 else 0

        discurso_156 = 'discurso_156' in request.form
        discurso_156 = 1 if discurso_156 else 0

        discurso_157 = 'discurso_157' in request.form
        discurso_157 = 1 if discurso_157 else 0

        discurso_158 = 'discurso_158' in request.form
        discurso_158 = 1 if discurso_158 else 0

        discurso_159 = 'discurso_159' in request.form
        discurso_159 = 1 if discurso_159 else 0

        discurso_160 = 'discurso_160' in request.form
        discurso_160 = 1 if discurso_160 else 0

        discurso_161 = 'discurso_161' in request.form
        discurso_161 = 1 if discurso_161 else 0

        discurso_162 = 'discurso_162' in request.form
        discurso_162 = 1 if discurso_162 else 0

        discurso_163 = 'discurso_163' in request.form
        discurso_163 = 1 if discurso_163 else 0

        discurso_164 = 'discurso_164' in request.form
        discurso_164 = 1 if discurso_164 else 0

        discurso_165 = 'discurso_165' in request.form
        discurso_165 = 1 if discurso_165 else 0

        discurso_166 = 'discurso_166' in request.form
        discurso_166 = 1 if discurso_166 else 0

        discurso_167 = 'discurso_167' in request.form
        discurso_167 = 1 if discurso_167 else 0

        discurso_168 = 'discurso_168' in request.form
        discurso_168 = 1 if discurso_168 else 0

        discurso_169 = 'discurso_169' in request.form
        discurso_169 = 1 if discurso_169 else 0

        discurso_170 = 'discurso_170' in request.form
        discurso_170 = 1 if discurso_170 else 0

        discurso_171 = 'discurso_171' in request.form
        discurso_171 = 1 if discurso_171 else 0

        discurso_172 = 'discurso_172' in request.form
        discurso_172 = 1 if discurso_172 else 0

        discurso_173 = 'discurso_173' in request.form
        discurso_173 = 1 if discurso_173 else 0

        discurso_174 = 'discurso_174' in request.form
        discurso_174 = 1 if discurso_174 else 0

        discurso_175 = 'discurso_175' in request.form
        discurso_175 = 1 if discurso_175 else 0

        discurso_176 = 'discurso_176' in request.form
        discurso_176 = 1 if discurso_176 else 0

        discurso_177 = 'discurso_177' in request.form
        discurso_177 = 1 if discurso_177 else 0

        discurso_178 = 'discurso_178' in request.form
        discurso_178 = 1 if discurso_178 else 0

        discurso_179 = 'discurso_179' in request.form
        discurso_179 = 1 if discurso_179 else 0

        discurso_180 = 'discurso_180' in request.form
        discurso_180 = 1 if discurso_180 else 0

        discurso_181 = 'discurso_181' in request.form
        discurso_181 = 1 if discurso_181 else 0

        discurso_182 = 'discurso_182' in request.form
        discurso_182 = 1 if discurso_182 else 0

        discurso_183 = 'discurso_183' in request.form
        discurso_183 = 1 if discurso_183 else 0

        discurso_184 = 'discurso_184' in request.form
        discurso_184 = 1 if discurso_184 else 0

        discurso_185 = 'discurso_185' in request.form
        discurso_185 = 1 if discurso_185 else 0

        discurso_186 = 'discurso_186' in request.form
        discurso_186 = 1 if discurso_186 else 0

        discurso_187 = 'discurso_187' in request.form
        discurso_187 = 1 if discurso_187 else 0

        discurso_188 = 'discurso_188' in request.form
        discurso_188 = 1 if discurso_188 else 0

        discurso_189 = 'discurso_189' in request.form
        discurso_189 = 1 if discurso_189 else 0

        discurso_190 = 'discurso_190' in request.form
        discurso_190 = 1 if discurso_190 else 0

        discurso_191 = 'discurso_191' in request.form
        discurso_191 = 1 if discurso_191 else 0

        discurso_192 = 'discurso_192' in request.form
        discurso_192 = 1 if discurso_192 else 0

        discurso_193 = 'discurso_193' in request.form
        discurso_193 = 1 if discurso_193 else 0

        discurso_194 = 'discurso_194' in request.form
        discurso_194 = 1 if discurso_194 else 0

                            
        cursor = g.bd.cursor()

        cursor.execute("""
            SELECT * FROM oradores WHERE nombres = ? AND apellidos = ?
        """, (nombres, apellidos))

        resultado = cursor.fetchone()

        if resultado:
            cursor.execute("""
                UPDATE oradores
                SET aprobado_para_salir = ?, correo_electronico = ?, celular = ?, telefono = ?, nombramiento = ?, discurso_1 = ?, discurso_2 = ?, discurso_3 = ?, discurso_4 = ?, discurso_5 = ?, discurso_6 = ?,
    discurso_7 = ?, discurso_8 = ?, discurso_9 = ?, discurso_10 = ?, discurso_11 = ?, discurso_12 = ?,
    discurso_13 = ?, discurso_14 = ?, discurso_15 = ?, discurso_16 = ?, discurso_17 = ?, discurso_18 = ?,
    discurso_19 = ?, discurso_20 = ?, discurso_21 = ?, discurso_22 = ?, discurso_23 = ?, discurso_24 = ?,
    discurso_25 = ?, discurso_26 = ?, discurso_27 = ?, discurso_28 = ?, discurso_29 = ?, discurso_30 = ?, 
    discurso_31 = ?, discurso_32 = ?, discurso_33 = ?, discurso_34 = ?, discurso_35 = ?, 
    discurso_36 = ?, discurso_37 = ?, discurso_38 = ?, discurso_39 = ?, discurso_40 = ?, 
    discurso_41 = ?, discurso_42 = ?, discurso_43 = ?, discurso_44 = ?, discurso_45 = ?, 
    discurso_46 = ?, discurso_47 = ?, discurso_48 = ?, discurso_49 = ?, discurso_50 = ?, discurso_51 = ?, discurso_52 = ?, discurso_53 = ?, discurso_54 = ?, discurso_55 = ?, 
    discurso_56 = ?, discurso_57 = ?, discurso_58 = ?, discurso_59 = ?, discurso_60 = ?, 
    discurso_61 = ?, discurso_62 = ?, discurso_63 = ?, discurso_64 = ?, discurso_65 = ?, 
    discurso_66 = ?, discurso_67 = ?, discurso_68 = ?, discurso_69 = ?, discurso_70 = ?, 
    discurso_71 = ?, discurso_72 = ?, discurso_73 = ?, discurso_74 = ?, discurso_75 = ?, discurso_76 = ?, discurso_77 = ?, discurso_78 = ?, discurso_79 = ?, discurso_80 = ?, 
    discurso_81 = ?, discurso_82 = ?, discurso_83 = ?, discurso_84 = ?, discurso_85 = ?, 
    discurso_86 = ?, discurso_87 = ?, discurso_88 = ?, discurso_89 = ?, discurso_90 = ?, 
    discurso_91 = ?, discurso_92 = ?, discurso_93 = ?, discurso_94 = ?, discurso_95 = ?, 
    discurso_96 = ?, discurso_97 = ?, discurso_98 = ?, discurso_99 = ?, discurso_100 = ?,
    discurso_101 = ?, discurso_102 = ?, discurso_103 = ?, discurso_104 = ?, discurso_105 = ?, 
    discurso_106 = ?, discurso_107 = ?, discurso_108 = ?, discurso_109 = ?, discurso_110 = ?, 
    discurso_111 = ?, discurso_112 = ?, discurso_113 = ?, discurso_114 = ?, discurso_115 = ?, 
    discurso_116 = ?, discurso_117 = ?, discurso_118 = ?, discurso_119 = ?, discurso_120 = ?, 
    discurso_121 = ?, discurso_122 = ?, discurso_123 = ?, discurso_124 = ?, discurso_125 = ?, discurso_126 = ?, discurso_127 = ?, discurso_128 = ?, discurso_129 = ?, discurso_130 = ?, 
    discurso_131 = ?, discurso_132 = ?, discurso_133 = ?, discurso_134 = ?, discurso_135 = ?, 
    discurso_136 = ?, discurso_137 = ?, discurso_138 = ?, discurso_139 = ?, discurso_140 = ?, 
    discurso_141 = ?, discurso_142 = ?, discurso_143 = ?, discurso_144 = ?, discurso_145 = ?, 
    discurso_146 = ?, discurso_147 = ?, discurso_148 = ?, discurso_149 = ?, discurso_150 = ?,
    discurso_151 = ?, discurso_152 = ?, discurso_153 = ?, discurso_154 = ?, discurso_155 = ?, 
    discurso_156 = ?, discurso_157 = ?, discurso_158 = ?, discurso_159 = ?, discurso_160 = ?, 
    discurso_161 = ?, discurso_162 = ?, discurso_163 = ?, discurso_164 = ?, discurso_165 = ?, 
    discurso_166 = ?, discurso_167 = ?, discurso_168 = ?, discurso_169 = ?, discurso_170 = ?, 
    discurso_171 = ?, discurso_172 = ?, discurso_173 = ?, discurso_174 = ?, discurso_175 = ?,
    discurso_176 = ?, discurso_177 = ?, discurso_178 = ?, discurso_179 = ?, discurso_180 = ?, 
    discurso_181 = ?, discurso_182 = ?, discurso_183 = ?, discurso_184 = ?, discurso_185 = ?, 
    discurso_186 = ?, discurso_187 = ?, discurso_188 = ?, discurso_189 = ?, discurso_190 = ?, 
    discurso_191 = ?, discurso_192 = ?, discurso_193 = ?, discurso_194 = ?, congregacion = ?
                WHERE nombres = ? AND apellidos = ?
            """, (aprobado_para_salir, correo_electronico, celular, telefono, nombramiento, discurso_1, discurso_2, discurso_3, discurso_4, discurso_5, discurso_6,
      discurso_7, discurso_8, discurso_9, discurso_10, discurso_11, discurso_12,
      discurso_13, discurso_14, discurso_15, discurso_16, discurso_17, discurso_18,
      discurso_19, discurso_20, discurso_21, discurso_22, discurso_23, discurso_24,
      discurso_25, discurso_26, discurso_27, discurso_28, discurso_29, discurso_30,
      discurso_31, discurso_32, discurso_33, discurso_34, discurso_35,
      discurso_36, discurso_37, discurso_38, discurso_39, discurso_40,
      discurso_41, discurso_42, discurso_43, discurso_44, discurso_45,
      discurso_46, discurso_47, discurso_48, discurso_49, discurso_50, discurso_51, discurso_52, discurso_53, discurso_54, discurso_55,
      discurso_56, discurso_57, discurso_58, discurso_59, discurso_60,
      discurso_61, discurso_62, discurso_63, discurso_64, discurso_65,
      discurso_66, discurso_67, discurso_68, discurso_69, discurso_70,
      discurso_71, discurso_72, discurso_73, discurso_74, discurso_75, discurso_76, discurso_77, discurso_78, discurso_79, discurso_80,
      discurso_81, discurso_82, discurso_83, discurso_84, discurso_85,
      discurso_86, discurso_87, discurso_88, discurso_89, discurso_90,
      discurso_91, discurso_92, discurso_93, discurso_94, discurso_95,
      discurso_96, discurso_97, discurso_98, discurso_99, discurso_100,
      discurso_101, discurso_102, discurso_103, discurso_104, discurso_105,
      discurso_106, discurso_107, discurso_108, discurso_109, discurso_110,
      discurso_111, discurso_112, discurso_113, discurso_114, discurso_115,
      discurso_116, discurso_117, discurso_118, discurso_119, discurso_120,
      discurso_121, discurso_122, discurso_123, discurso_124, discurso_125, discurso_126, discurso_127, discurso_128, discurso_129, discurso_130,
      discurso_131, discurso_132, discurso_133, discurso_134, discurso_135,
      discurso_136, discurso_137, discurso_138, discurso_139, discurso_140,
      discurso_141, discurso_142, discurso_143, discurso_144, discurso_145,
      discurso_146, discurso_147, discurso_148, discurso_149, discurso_150,
      discurso_151, discurso_152, discurso_153, discurso_154, discurso_155,
      discurso_156, discurso_157, discurso_158, discurso_159, discurso_160,
      discurso_161, discurso_162, discurso_163, discurso_164, discurso_165,
      discurso_166, discurso_167, discurso_168, discurso_169, discurso_170,
      discurso_171, discurso_172, discurso_173, discurso_174, discurso_175,
      discurso_176, discurso_177, discurso_178, discurso_179, discurso_180,
      discurso_181, discurso_182, discurso_183, discurso_184, discurso_185,
      discurso_186, discurso_187, discurso_188, discurso_189, discurso_190,
      discurso_191, discurso_192, discurso_193, discurso_194, congregacion, nombres, apellidos))
        else:
            cursor.execute("""
                INSERT INTO oradores (nombres, apellidos, aprobado_para_salir, correo_electronico, celular, telefono, nombramiento, discurso_1, discurso_2, discurso_3, discurso_4, discurso_5, discurso_6,
      discurso_7, discurso_8, discurso_9, discurso_10, discurso_11, discurso_12,
      discurso_13, discurso_14, discurso_15, discurso_16, discurso_17, discurso_18,
      discurso_19, discurso_20, discurso_21, discurso_22, discurso_23, discurso_24,
      discurso_25, discurso_26, discurso_27, discurso_28, discurso_29, discurso_30,
      discurso_31, discurso_32, discurso_33, discurso_34, discurso_35,
      discurso_36, discurso_37, discurso_38, discurso_39, discurso_40,
      discurso_41, discurso_42, discurso_43, discurso_44, discurso_45,
      discurso_46, discurso_47, discurso_48, discurso_49, discurso_50, discurso_51, discurso_52, discurso_53, discurso_54, discurso_55,
      discurso_56, discurso_57, discurso_58, discurso_59, discurso_60,
      discurso_61, discurso_62, discurso_63, discurso_64, discurso_65,
      discurso_66, discurso_67, discurso_68, discurso_69, discurso_70,
      discurso_71, discurso_72, discurso_73, discurso_74, discurso_75, discurso_76, discurso_77, discurso_78, discurso_79, discurso_80,
      discurso_81, discurso_82, discurso_83, discurso_84, discurso_85,
      discurso_86, discurso_87, discurso_88, discurso_89, discurso_90,
      discurso_91, discurso_92, discurso_93, discurso_94, discurso_95,
      discurso_96, discurso_97, discurso_98, discurso_99, discurso_100,
      discurso_101, discurso_102, discurso_103, discurso_104, discurso_105,
      discurso_106, discurso_107, discurso_108, discurso_109, discurso_110,
      discurso_111, discurso_112, discurso_113, discurso_114, discurso_115,
      discurso_116, discurso_117, discurso_118, discurso_119, discurso_120,
      discurso_121, discurso_122, discurso_123, discurso_124, discurso_125, discurso_126, discurso_127, discurso_128, discurso_129, discurso_130,
      discurso_131, discurso_132, discurso_133, discurso_134, discurso_135,
      discurso_136, discurso_137, discurso_138, discurso_139, discurso_140,
      discurso_141, discurso_142, discurso_143, discurso_144, discurso_145,
      discurso_146, discurso_147, discurso_148, discurso_149, discurso_150,
      discurso_151, discurso_152, discurso_153, discurso_154, discurso_155,
      discurso_156, discurso_157, discurso_158, discurso_159, discurso_160,
      discurso_161, discurso_162, discurso_163, discurso_164, discurso_165,
      discurso_166, discurso_167, discurso_168, discurso_169, discurso_170,
      discurso_171, discurso_172, discurso_173, discurso_174, discurso_175,
      discurso_176, discurso_177, discurso_178, discurso_179, discurso_180,
      discurso_181, discurso_182, discurso_183, discurso_184, discurso_185,
      discurso_186, discurso_187, discurso_188, discurso_189, discurso_190,
      discurso_191, discurso_192, discurso_193, discurso_194, congregacion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nombres, apellidos, aprobado_para_salir, correo_electronico, celular, telefono, nombramiento, discurso_1, discurso_2, discurso_3, discurso_4, discurso_5, discurso_6,
      discurso_7, discurso_8, discurso_9, discurso_10, discurso_11, discurso_12,
      discurso_13, discurso_14, discurso_15, discurso_16, discurso_17, discurso_18,
      discurso_19, discurso_20, discurso_21, discurso_22, discurso_23, discurso_24,
      discurso_25, discurso_26, discurso_27, discurso_28, discurso_29, discurso_30,
      discurso_31, discurso_32, discurso_33, discurso_34, discurso_35,
      discurso_36, discurso_37, discurso_38, discurso_39, discurso_40,
      discurso_41, discurso_42, discurso_43, discurso_44, discurso_45,
      discurso_46, discurso_47, discurso_48, discurso_49, discurso_50, discurso_51, discurso_52, discurso_53, discurso_54, discurso_55,
      discurso_56, discurso_57, discurso_58, discurso_59, discurso_60,
      discurso_61, discurso_62, discurso_63, discurso_64, discurso_65,
      discurso_66, discurso_67, discurso_68, discurso_69, discurso_70,
      discurso_71, discurso_72, discurso_73, discurso_74, discurso_75, discurso_76, discurso_77, discurso_78, discurso_79, discurso_80,
      discurso_81, discurso_82, discurso_83, discurso_84, discurso_85,
      discurso_86, discurso_87, discurso_88, discurso_89, discurso_90,
      discurso_91, discurso_92, discurso_93, discurso_94, discurso_95,
      discurso_96, discurso_97, discurso_98, discurso_99, discurso_100,
      discurso_101, discurso_102, discurso_103, discurso_104, discurso_105,
      discurso_106, discurso_107, discurso_108, discurso_109, discurso_110,
      discurso_111, discurso_112, discurso_113, discurso_114, discurso_115,
      discurso_116, discurso_117, discurso_118, discurso_119, discurso_120,
      discurso_121, discurso_122, discurso_123, discurso_124, discurso_125, discurso_126, discurso_127, discurso_128, discurso_129, discurso_130,
      discurso_131, discurso_132, discurso_133, discurso_134, discurso_135,
      discurso_136, discurso_137, discurso_138, discurso_139, discurso_140,
      discurso_141, discurso_142, discurso_143, discurso_144, discurso_145,
      discurso_146, discurso_147, discurso_148, discurso_149, discurso_150,
      discurso_151, discurso_152, discurso_153, discurso_154, discurso_155,
      discurso_156, discurso_157, discurso_158, discurso_159, discurso_160,
      discurso_161, discurso_162, discurso_163, discurso_164, discurso_165,
      discurso_166, discurso_167, discurso_168, discurso_169, discurso_170,
      discurso_171, discurso_172, discurso_173, discurso_174, discurso_175,
      discurso_176, discurso_177, discurso_178, discurso_179, discurso_180,
      discurso_181, discurso_182, discurso_183, discurso_184, discurso_185,
      discurso_186, discurso_187, discurso_188, discurso_189, discurso_190,
      discurso_191, discurso_192, discurso_193, discurso_194, congregacion))

        g.bd.commit() 

    return redirect('/oradores.html')

@app.route('/eliminar_orador/<int:id>', methods=['GET'])
def eliminar_orador(id):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM oradores WHERE id = ?", (id,))
    g.bd.commit()
    return redirect('/oradores.html')

@app.route('/eliminar_contenido_configuracion', methods=['GET'])
def eliminar_contenido_configuracion():
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM congregacion")
    cursor.execute("DELETE FROM configuracion")
    cursor.execute("DELETE FROM bosquejos")
    cursor.execute("DELETE FROM familias")
    cursor.execute("DELETE FROM grupos_predicacion")
    cursor.execute("DELETE FROM oradores")
    cursor.execute("DELETE FROM publicadores")
    g.bd.commit()
    return redirect('/')

@app.route('/nuevo_orador')
def nuevo_orador():
    return render_template('/detalle-orador.html', orador=None)

@app.route('/bosquejos.html')
def bosquejos():
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM oradores")
    oradoreslist = cursor.fetchall()

    cursor.execute("SELECT * FROM bosquejos")
    bosquejos_list = cursor.fetchall()  

    cursor.execute("SELECT nombre_congregacion FROM congregacion")
    congregacion = cursor.fetchone()

    if congregacion and congregacion[0].strip():
        congregacion_formateada = congregacion[0].strip("()'")
    else:
        congregacion_formateada = None 

    return render_template('bosquejos.html', oradoreslist=oradoreslist, bosquejos_list=bosquejos_list, congregacion=congregacion_formateada)


@app.route('/nuevo_bosquejo', methods=['GET'])
def nuevo_bosquejo():
    nombres = request.args.get('nombres')
    apellidos = request.args.get('apellidos')
    congregacion = request.args.get('congregacion')

    cursor = g.bd.cursor()
    
    cursor.execute("SELECT id FROM oradores WHERE nombres = ? AND apellidos = ? AND congregacion = ?", (nombres, apellidos, congregacion))
    orador_existente = cursor.fetchone()

    if not orador_existente:
        cursor.execute("INSERT INTO oradores (nombres, apellidos, congregacion) VALUES (?, ?, ?)", (nombres, apellidos, congregacion))
        g.bd.commit()
        
        cursor.execute("SELECT last_insert_rowid()")
        orador_id = cursor.fetchone()[0]
    else:
        orador_id = orador_existente[0]
    
    cursor.execute("INSERT INTO bosquejos (id_orador, nombres, apellidos, congregacion) VALUES (?, ?, ?, ?)", (orador_id, nombres, apellidos, congregacion))
    g.bd.commit()
    
    return redirect(url_for('bosquejos'))


@app.route('/mostrar_bosquejo/<int:id>', methods=['GET'])
def mostrar_bosquejo(id):
    cursor = g.bd.cursor()

    cursor.execute("SELECT * FROM bosquejos WHERE id_orador = ?", (id,))
    bosquejo = cursor.fetchone()

    cursor.execute("SELECT nombre_grupo FROM grupos_predicacion WHERE asignar_hospitalidad = 1")
    grupos = cursor.fetchall()

    cursor.execute("SELECT * FROM oradores WHERE id = ?", (id,))
    orador = cursor.fetchone()

    columnas_con_uno = obtener_columnas_con_uno(id)

    return render_template('/detalle-bosquejo.html', bosquejo=bosquejo, grupo=None, grupos_list=grupos, columnas_con_uno=columnas_con_uno)

def obtener_columnas_con_uno(id):
    cursor = g.bd.cursor()
    cursor.execute("PRAGMA table_info(oradores)")
    columnas = [row[1] for row in cursor.fetchall()]
    columnas_con_uno = []
    for columna in columnas:
        cursor.execute("SELECT {} FROM oradores WHERE id = ? AND {} = 1".format(columna, columna), (id,))
        resultado = cursor.fetchone()
        if resultado:
            columnas_con_uno.append(columna)
    return columnas_con_uno

@app.route('/guardar_bosquejo', methods=['POST'])
def guardar_bosquejo():
    if request.method == 'POST':
        id_orador = request.form['id']
        numero = request.form['discurso_numero']
        fecha = request.form['fecha_impartido']
        hospitalidad = request.form.get('hospitalidad', None)
        congregacion_visitar = request.form.get('congregacion_visitar', None)
        se_ha_quedado_hospitalidad_checkbox = 1 if 'se_ha_quedado_hospitalidad_checkbox' in request.form else 0
        se_ha_presentado_tiempo_checkbox = 1 if 'se_ha_presentado_tiempo_checkbox' in request.form else 0
        se_ha_presentado_discurso_checkbox = 1 if 'se_ha_presentado_discurso_checkbox' in request.form else 0
        anotaciones = request.form['anotaciones']

        cursor = g.bd.cursor()
        cursor.execute("""
            UPDATE bosquejos SET numero = ?, fecha = ?, hospitalidad = ?, 
                                   se_ha_quedado_hospitalidad_checkbox = ?, 
                                   se_ha_presentado_tiempo_checkbox = ?, 
                                   se_ha_presentado_discurso_checkbox = ?, 
                                   anotaciones = ?, congregacion_visitar = ? WHERE id_orador = ?
        """, (numero, fecha, hospitalidad, se_ha_quedado_hospitalidad_checkbox,
              se_ha_presentado_tiempo_checkbox, se_ha_presentado_discurso_checkbox, anotaciones, congregacion_visitar, id_orador))
        g.bd.commit()

        return redirect(url_for('bosquejos'))

@app.route('/eliminar_bosquejo/<int:id>', methods=['GET'])
def eliminar_bosquejo(id):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM bosquejos WHERE id_orador = ?", (id,))
    g.bd.commit()
    return redirect('/bosquejos.html')

@app.route('/estudio-atalaya.html')
def estudio_atalaya():
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM estudio_atalaya")
    estudios_atalayas = cursor.fetchall()  

    cursor.execute("SELECT nombre_congregacion FROM congregacion")
    congregacion = cursor.fetchone()

    if congregacion and congregacion[0].strip():
        congregacion_formateada = congregacion[0].strip("()'")
    else:
        congregacion_formateada = None 

    return render_template('estudio-atalaya.html', estudios_atalayas=estudios_atalayas, congregacion=congregacion_formateada)

@app.route('/mostrar_estudio_atalaya/<int:id>', methods=['GET'])
def mostrar_estudio_atalaya(id):
    cursor = g.bd.cursor()

    cursor.execute("SELECT * FROM estudio_atalaya WHERE id = ?", (id,))
    detalle_estalaya = cursor.fetchone()

    cursor.execute("SELECT nombres || ' ' || apellidos AS nombre_completo FROM publicadores WHERE checkbox_presidente_reunion_publica = 1")
    presidentes = cursor.fetchall()

    presidentes_formateados = [presidente[0].strip("('')") for presidente in presidentes]

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_oracion = 1")
    aprobados_oracion_inicio = cursor.fetchall()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_lector = 1")
    lectores = cursor.fetchall()

    return render_template('/detalle-estudio-atalaya.html', detalle_estalaya=detalle_estalaya, presidentes=presidentes_formateados, aprobados_oracion_inicio=aprobados_oracion_inicio, lectores=lectores)

@app.route('/nuevo-estudio-atalaya', methods=['GET'])
def nuevo_estudio_atalaya():
    cursor = g.bd.cursor()
    cursor.execute("SELECT nombres || ' ' || apellidos AS nombre_completo FROM publicadores WHERE checkbox_presidente_reunion_publica = 1")
    presidentes = cursor.fetchall()

    presidentes_formateados = [presidente[0].strip("('')") for presidente in presidentes]

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_oracion = 1")
    aprobados_oracion_inicio = cursor.fetchall()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_lector = 1")
    lectores = cursor.fetchall()

    return render_template('detalle-estudio-atalaya.html', detalle_estalaya=None, presidentes=presidentes_formateados, aprobados_oracion_inicio=aprobados_oracion_inicio, lectores=lectores)

@app.route('/guardar_estudio_atalaya', methods=['POST'])
def guardar_estudio_atalaya():
    id_estudio = request.form['id']
    fecha = request.form['fecha']
    presidente = request.form['presidente']
    oracion_inicio = request.form['oracion_inicio']
    lector_atalaya = request.form['lector_atalaya']
    oracion_final = request.form['oracion_final']

    cursor = g.bd.cursor()

    cursor.execute("SELECT * FROM estudio_atalaya WHERE id = ?", (id_estudio,))
    existing_estudio = cursor.fetchone()

    if existing_estudio:
        cursor.execute("UPDATE estudio_atalaya SET fecha=?, presidente=?, oracion_inicio=?, lector_atalaya=?, oracion_final=? WHERE id=?",
                        (fecha, presidente, oracion_inicio, lector_atalaya, oracion_final, id_estudio))

    else:
        cursor.execute("INSERT INTO estudio_atalaya (fecha, presidente, oracion_inicio, lector_atalaya, oracion_final) VALUES (?, ?, ?, ?, ?)",
                        (fecha, presidente, oracion_inicio, lector_atalaya, oracion_final))

    g.bd.commit()

    return redirect('/estudio-atalaya.html')

@app.route('/eliminar_estudio_atalaya/<int:id>', methods=['GET'])
def eliminar_estudio_atalaya(id):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM estudio_atalaya WHERE id = ?", (id,))
    g.bd.commit()
    return redirect('/estudio-atalaya.html')

@app.route('/vida-ministerio.html')
def vida_ministerio():
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM vida_ministerio")
    vida_ministerio = cursor.fetchall() 

    cursor.execute("SELECT nombre_congregacion FROM congregacion")
    congregacion = cursor.fetchone()
    
    if congregacion and congregacion[0].strip():
        congregacion_formateada = congregacion[0].strip("()'")
    else:
        congregacion_formateada = None 

    return render_template('vida-ministerio.html', congregacion=congregacion_formateada, vidas_ministerio=vida_ministerio)

@app.route('/nuevo-vida-ministerio', methods=['GET'])
def nuevo_vida_ministerio():
    current_year = request.args.get('year', datetime.datetime.now().year)
    current_week = request.args.get('week', datetime.datetime.now().isocalendar()[1])
    week_info, data = extract_data_from_WOL(current_year, current_week)
    url_previous, url_next = get_previous_and_next_urls(current_year, current_week)

    cursor = g.bd.cursor()
    cursor.execute("SELECT nombres || ' ' || apellidos AS nombre_completo FROM publicadores WHERE checkbox_presidente = 1")
    presidentes = cursor.fetchall()

    presidentes_formateados = [presidente[0].strip("('')") for presidente in presidentes]

    cursor.execute("SELECT nombres || ' ' || apellidos AS nombre_completo FROM publicadores WHERE checkbox_oracion = 1")
    oradores = cursor.fetchall()

    oradores_formateados = [orador[0].strip("('')") for orador in oradores]

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_estudio_biblico_congregacion = 1")
    conductores = cursor.fetchall()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_lector = 1")
    lectores = cursor.fetchall()

    cursor.execute("SELECT nombres, apellidos FROM publicadores")
    publicadores = cursor.fetchall()

    cursor.execute("SELECT nombres, apellidos FROM publicadores WHERE checkbox_discurso = 1")
    discursantes = cursor.fetchall()

    session['data'] = data

    return render_template('detalle-vida-ministerio.html', data=data, week_info=week_info, url_previous=url_previous, url_next=url_next, presidentes=presidentes_formateados, oradores=oradores_formateados, conductores=conductores, lectores=lectores, publicadores=publicadores, discursantes=discursantes)

def extract_data_from_WOL(year, week):
    url = f"https://wol.jw.org/es/wol/meetings/r4/lp-s/{year}/{week}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    week_info = soup.find('h1').text
    data = {}
    current_h2 = None

    for element in soup.find_all(['h2', 'h3']):
        if element.name == 'h2':
            current_h2 = element.text.strip()
            data[current_h2] = []
        elif element.name == 'h3' and current_h2:
            data[current_h2].append(element.text.strip())

    return week_info, data

def get_previous_and_next_urls(year, week):
    # Calcular la semana anterior
    previous_week_date = datetime.datetime.strptime(f"{year}-{week}-1", "%Y-%W-%w") - datetime.timedelta(weeks=1)
    previous_year = previous_week_date.year
    previous_week = previous_week_date.isocalendar()[1]
    url_previous = f"/nuevo-vida-ministerio?year={previous_year}&week={previous_week}"

    # Calcular la semana siguiente
    next_week_date = datetime.datetime.strptime(f"{year}-{week}-1", "%Y-%W-%w") + datetime.timedelta(weeks=1)
    next_year = next_week_date.year
    next_week = next_week_date.isocalendar()[1]
    url_next = f"/nuevo-vida-ministerio?year={next_year}&week={next_week}"

    return url_previous, url_next

@app.route('/guardar_vida_ministerio', methods=['POST'])
def guardar_vida_ministerio():
    data = session.get('data', {})
    week_info = request.form.get('week_info')
    presidente = request.form.get('presidente')
    oracion_inicio = request.form.get('oracion_inicio')
    oracion_final = request.form.get('oracion_final')

    form_data = {
        "week_info": week_info,
        "presidente": presidente,
        "oracion_inicio": oracion_inicio,
        "oracion_final": oracion_final,
        "temas": []
    }

    for h2, h3_list in data.items():
        tema = {"titulo": h2, "detalles": []}
        for h3 in h3_list:
            if "Estudio bíblico de la congregación" in h3:
                conductor = request.form.get(f"conductor_{h3}")
                lector = request.form.get(f"lector_{h3}")
                detalle = {"subtitulo": h3, "conductor": conductor, "lector": lector}
            else:
                publicador = request.form.get(f"publicador_{h3}")
                ayudante = request.form.get(f"ayudante_{h3}")
                detalle = {"subtitulo": h3, "publicador": publicador, "ayudante": ayudante}
            tema["detalles"].append(detalle)
        form_data["temas"].append(tema)

    # Convierte el diccionario a una cadena JSON
    form_data_json = json.dumps(form_data, ensure_ascii=False, indent=4)

    # Guarda en la base de datos
    cursor = g.bd.cursor()
    cursor.execute("""
        INSERT INTO vida_ministerio (week_info, presidente, oracion_inicio, oracion_final, datos_json)
        VALUES (?, ?, ?, ?, ?)
    """, (week_info, presidente, oracion_inicio, oracion_final, form_data_json))

    g.bd.commit()

    return redirect(url_for('vida_ministerio'))

def obtener_semana_de_la_base_de_datos(week_id):
    # Obtener la conexión a la base de datos existente
    cursor = g.bd.cursor()

    # Ejecutar la consulta SQL para obtener la semana por su ID
    cursor.execute("SELECT datos_json FROM vida_ministerio WHERE id = ?", (week_id,))
    
    # Obtener el resultado de la consulta
    semana = cursor.fetchone()

    if semana:
        # Si se encuentra la semana, obtener el JSON de la columna datos_json
        datos_json = semana[0]
        
        # Convertir el JSON a un diccionario de Python
        semana_dict = json.loads(datos_json)
        return semana_dict
    else:
        # Manejo de casos donde no se encuentra la semana con el ID dado
        return None

@app.route('/mostrar_vida_ministerio/<int:id>')
def mostrar_vida_ministerio(id):
    cursor = g.bd.cursor()
    # Aquí debes obtener los datos de la semana de la base de datos usando el ID de la semana (week_id)
    semana = obtener_semana_de_la_base_de_datos(id)

    cursor.execute("SELECT * FROM vida_ministerio")
    vida_ministerio = cursor.fetchone()
   
    cursor.execute("SELECT nombre_congregacion FROM congregacion")
    congregacion = cursor.fetchone()

    if congregacion and congregacion[0].strip():
        congregacion_formateada = congregacion[0].strip("()'")
    else:
        congregacion_formateada = None 
    
    # Aquí renderizas el template con los datos obtenidos de la base de datos
    return render_template('mostrar-vida-ministerio.html', semana=semana, congregacion=congregacion_formateada, vida_ministerio=vida_ministerio)

@app.route('/visita-superint-circuito.html')
def visita_superint_circuito():
    return render_template('visita-superint-circuito.html')

@app.route('/nueva-actividad')
def nueva_actividad_visita_superint_circuito():
    return render_template('detalle-visita-superint-circuito.html')

# Nueva función para verificar la existencia de la tabla
def table_exists(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None

@app.before_request
def load_user_info():
    if request.endpoint is not None and 'login' not in request.endpoint:
        # Código para cargar la información del usuario
        # Evitar cargar info de usuario en la página de login
        user_db = get_user_db()
        if user_db:
            cursor = user_db.cursor()
            if table_exists(cursor, 'configuracion'):
                cursor.execute("SELECT nombre, apellidos, user_email FROM configuracion WHERE id = ?", (1,))
                configuracion_data = cursor.fetchone()
                
                if configuracion_data:
                    nombre, apellidos, user_email = configuracion_data
                    
                    # Verificar si los campos están vacíos o nulos y asignar valores predeterminados si es necesario
                    g.nombre = nombre if nombre and nombre.strip() else "Nombres"
                    g.apellidos = apellidos if apellidos and apellidos.strip() else "Apellidos"
                    g.user_email = user_email if user_email and user_email.strip() else "usuario@correo.com"
                else:
                    # Si no se encuentra ninguna fila, asignar valores predeterminados
                    g.nombre, g.apellidos, g.user_email = "Nombres", "Apellidos", "usuario@correo.com"
            else:
                # Si la tabla no existe, asignar valores predeterminados
                g.nombre, g.apellidos, g.user_email = "Nombres", "Apellidos", "usuario@correo.com"

@app.context_processor
def inject_user_info():
    return dict(nombre=g.get('nombre', 'Nombre'), apellidos=g.get('apellidos', 'Apellidos'), email=g.get('user_email', 'usuario@correo.com'))

@app.route('/accessing', methods=['POST'])
def accessing():
    email = request.form['email']
    password = request.form['password']
    
    # Crear una conexión directa a cavea.db
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, database, contraseña, golden_edition FROM emptor WHERE correo = ?", (email,))
    result = cursor.fetchone()
    
    if result and result['contraseña'] == password:
        user_id = result['id']
        user_db_name = result['database']
        user_golden_edition = result['golden_edition']
        session['user_db'] = user_db_name
        session['user_id'] = user_id
        session['user_ge'] = user_golden_edition
        logging.debug(f"Usuario {email} ha iniciado sesión. Conectado a la base de datos del usuario: {user_db_name}. ¿Es Golden Edition?: {user_golden_edition}")
        
        # Actualizar el último inicio de sesión del usuario
        update_last_login(user_id)
        last_login = get_last_login(user_id)
        
        # Enviar correo electrónico de notificación
        requester_ip = get_requester_ip()
        sender = app.config['MAIL_USERNAME']
        send_login_notification(sender, email, email, last_login, requester_ip)
        
        conn.close()
        return redirect(url_for('index'))
    else:
        conn.close()
        flash('Correo o contraseña incorrectos.')
        return redirect(url_for('login'))

@app.route('/signup')
def signup():
    return render_template('signup.html') 

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')  

@app.route('/recovery', methods=['POST'])
def recovery():
    email = request.form['email']
    
    # Crear una conexión directa a cavea.db
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT contraseña FROM emptor WHERE correo = ?", (email,))
    result = cursor.fetchone()
    
    if result:
        password = result['contraseña']  # Obtiene la contraseña de la base de datos
        requester_ip = get_requester_ip()
        sender = app.config['MAIL_USERNAME']
        send_password_email(sender, email, password, requester_ip)

        conn.close()
        flash('Se ha enviado la contraseña a tu correo electrónico.')
        return redirect(url_for('login'))
    else:
        conn.close()
        flash('El correo electrónico no está registrado en nuestra base de datos.')
        return redirect(url_for('forgot'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emptor WHERE correo = ?", (email,))
        user = cursor.fetchone()
        
        if user:
            flash('El usuario ya existe. Por favor, selecciona la opción de reenviar token.')
            return redirect(url_for('resend_token', email=email))
        else:
            token = secrets.token_urlsafe(16)
            token_expiration = datetime.datetime.now() + timedelta(hours=1)
            confirm_url = url_for('confirm_email', token=token, _external=True)
            requester_ip = get_requester_ip()
            sender = app.config['MAIL_USERNAME']
            send_email(sender, email, confirm_url, requester_ip)
            
            cursor.execute("INSERT INTO emptor (correo, token, token_expiration, database) VALUES (?, ?, ?, ?)", (email, token, token_expiration, f'{email.split("@")[0]}.db'))
            conn.commit()
            conn.close()
            
            try:
                shutil.copy("kha.db", f"{email.split('@')[0]}.db")
            except FileNotFoundError:
                flash('Error: la base de datos "kha.db" no se encontró.')
                return redirect(url_for('register'))
            except Exception as e:
                flash(f'Error al copiar la base de datos: {str(e)}')
                return redirect(url_for('register'))
            
            user_db_name = f"{email.split('@')[0]}.db"
            if not os.path.exists(user_db_name):
                user_conn = sqlite3.connect(user_db_name)
                user_cursor = user_conn.cursor()
                user_cursor.execute("CREATE TABLE IF NOT EXISTS user_data (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT)")
                user_conn.commit()
                user_conn.close()
            
            flash('Se ha enviado un enlace de confirmación a tu correo.')
            return redirect(url_for('register'))
    return render_template('signup.html')

@app.route('/resend_token/<email>', methods=['GET', 'POST'])
def resend_token(email):
    if request.method == 'POST' or request.method == 'GET':
        token = secrets.token_urlsafe(16)
        token_expiration = datetime.datetime.now() + timedelta(hours=24)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        requester_ip = get_requester_ip()
        sender = app.config['MAIL_USERNAME']
        send_email(sender, email, confirm_url, requester_ip)
        
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE emptor SET token = ?, token_expiration = ? WHERE correo = ?", (token, token_expiration, email))
        conn.commit()
        conn.close()
        
        flash('Se ha reenviado un nuevo enlace de confirmación a tu correo.')
        return redirect(url_for('register'))
    return render_template('signup.html', email=email)


def get_requester_ip():
    if request.headers.get('X-Forwarded-For'):
        # Para soportar aplicaciones detrás de un proxy como nginx
        ip = request.headers.getlist('X-Forwarded-For')[0]
    else:
        ip = request.remote_addr
    return ip

def send_login_notification(sender, recipient, email, last_login, requester_ip):
    msg = Message('Nuevo inicio de sesión en Kingdom Hall Attendant', sender=sender, recipients=[recipient])
    # Cuerpo del mensaje en HTML
    msg.html = f"""
    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <title> </title>
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style type="text/css">
        #outlook a {{
          padding: 0;
        }}

        body {{
          margin: 0;
          padding: 0;
          -webkit-text-size-adjust: 100%;
          -ms-text-size-adjust: 100%;
        }}

        table,
        td {{
          border-collapse: collapse;
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
        }}

        img {{
          border: 0;
          height: auto;
          line-height: 100%;
          outline: none;
          text-decoration: none;
          -ms-interpolation-mode: bicubic;
        }}

        p {{
          display: block;
          margin: 13px 0;
        }}
      </style>
      <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
      <![endif]-->
      <!--[if lte mso 11]>
        <style type="text/css">
          .outlook-group-fix {{ width:100% !important; }}
        </style>
      <![endif]-->
      <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
      <style type="text/css">
        @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
      </style>
      <style type="text/css">
        @media only screen and (min-width:480px) {{
          .mj-column-per-100 {{
            width: 100% !important;
            max-width: 100%;
          }}
        }}
      </style>
      <style type="text/css">
        @media only screen and (max-width:480px) {{
          table.full-width-mobile {{
            width: 100% !important;
          }}
          td.full-width-mobile {{
            width: auto !important;
          }}
        }}
      </style>
      <style type="text/css">
        * {{
          text-rendering: optimizeLegibility;
          -moz-osx-font-smoothing: grayscale;
          font-smoothing: antialiased;
          -webkit-font-smoothing: antialiased;
        }}

        .type-cta {{
          user-select: none;
        }}

        .type-nostyle {{
          text-decoration: none;
        }}

        p {{
          margin-top: 0;
        }}
      </style>
    </head>

    <body style="background-color:white;">
      <div style="background-color:white;">
        <!-- logo -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:64px 10% 12px 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:54px;"> <a href="https://www.getkha.org" target="_blank">
                                  <img alt="kingdom hall attendant logo" height="auto" src="https://www.getkha.org/static/images/313010479-cfab1393-8ae1-4b3f-9895-7022272f1262.jpeg" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;border-radius:25%;" width="54"/>
                                </a> </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body head -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:12px 10% 4px 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:8px 0 0 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:22px;font-weight:600;line-height:1.2;text-align:center;color:#000000;">Nuevo inicio de sesión en Kingdom Hall Attendant</div>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body content -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:16px 16px 0 16px;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:488px;"> <img alt="kingdom hall attendant subscribe loader" height="auto" src="https://assets.dekks.app/mails/marketing/dekks-loader.gif" style="border:0;border-radius:12px;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="488" /> </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body content -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:12px 10% 0 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                    <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                      <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Notamos que iniciaste sesión.</span> Si fuiste tú, puedes ignorar este correo.</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                      <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;">Ubicación: {requester_ip}<br>Hora: {last_login}</div>
                    </td>
                  </tr>
                      <tr>
                    <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                      <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;">¿No fuiste tú? Tómate unos minutos para proteger tu cuenta.</div>
                    </td>
                  </tr>
                      <tr>
                        <td style="font-size:0px;word-break:break-word;">
                          <div style="height:8px;"> &nbsp; </div>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" vertical-align="middle" class="type-cta" style="font-size:0px;padding:0 0 32px 0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                            <tr>
                              <td align="center" bgcolor="#2e2c35" role="presentation" style="border:none;border-radius:6px;color:white;cursor:auto;padding:14px 24px;" valign="middle"> <a href="https://www.getkha.org/login" style="background:#2e2c35;color:white;font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:16px;font-weight:600;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">
                                Proteger cuenta
                              </a> </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      
                      <tr>
                        <td align="center" style="font-size:0px;padding:24px 16px;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:10px;font-weight:300;line-height:1.2;text-align:center;color:#8E8E92;">© 2024 Kingdom Hall Attendant. Todos los derechos reservados.</div>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </body>

    </html>
    """
    mail.send(msg)

def send_email(sender, recipient, confirm_url, requester_ip):
    msg = Message('Kingdom Hall Attendant: Completa tu registro', sender=sender, recipients=[recipient])
    # Cuerpo del mensaje en HTML
    msg.html = f"""
    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <title> </title>
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style type="text/css">
        #outlook a {{
          padding: 0;
        }}

        body {{
          margin: 0;
          padding: 0;
          -webkit-text-size-adjust: 100%;
          -ms-text-size-adjust: 100%;
        }}

        table,
        td {{
          border-collapse: collapse;
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
        }}

        img {{
          border: 0;
          height: auto;
          line-height: 100%;
          outline: none;
          text-decoration: none;
          -ms-interpolation-mode: bicubic;
        }}

        p {{
          display: block;
          margin: 13px 0;
        }}
      </style>
      <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
      <![endif]-->
      <!--[if lte mso 11]>
        <style type="text/css">
          .outlook-group-fix {{ width:100% !important; }}
        </style>
      <![endif]-->
      <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
      <style type="text/css">
        @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
      </style>
      <style type="text/css">
        @media only screen and (min-width:480px) {{
          .mj-column-per-100 {{
            width: 100% !important;
            max-width: 100%;
          }}
        }}
      </style>
      <style type="text/css">
        @media only screen and (max-width:480px) {{
          table.full-width-mobile {{
            width: 100% !important;
          }}
          td.full-width-mobile {{
            width: auto !important;
          }}
        }}
      </style>
      <style type="text/css">
        * {{
          text-rendering: optimizeLegibility;
          -moz-osx-font-smoothing: grayscale;
          font-smoothing: antialiased;
          -webkit-font-smoothing: antialiased;
        }}

        .type-cta {{
          user-select: none;
        }}

        .type-nostyle {{
          text-decoration: none;
        }}

        p {{
          margin-top: 0;
        }}
      </style>
    </head>

    <body style="background-color:white;">
      <div style="background-color:white;">
        <!-- logo -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:64px 10% 12px 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:54px;"> <a href="https://www.getkha.org" target="_blank">
                                  <img alt="kingdom hall attendant logo" height="auto" src="https://www.getkha.org/static/images/313010479-cfab1393-8ae1-4b3f-9895-7022272f1262.jpeg" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;border-radius:25%;" width="54"/>
                                </a> </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body head -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:12px 10% 4px 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:8px 0 0 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:22px;font-weight:600;line-height:1.2;text-align:center;color:#000000;">Hola. Gracias por registrarte 👏</div>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body content -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:16px 16px 0 16px;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:488px;"> <img alt="kingdom hall attendant subscribe loader" height="auto" src="https://assets.dekks.app/mails/marketing/dekks-loader.gif" style="border:0;border-radius:12px;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="488" /> </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body content -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:12px 10% 0 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Ya casi terminas.</span> Confirma tu correo electrónico y presiona el botón a continuación. No hacemos spam ✌️</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">You're almost done.</span> Confirm your email and press the button below. We don't spam ✌️</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Hai quasi finito.</span> Conferma la tua email e premi il pulsante qui sotto. Non inviamo spam ✌️</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Vous avez presque fini.</span> Confirmez votre email et appuyez sur le bouton ci-dessous. Nous ne spammons pas ✌️</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Você está quase pronto.</span> Confirme seu e-mail e pressione o botão abaixo. Não enviamos spam ✌️</div>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size:0px;word-break:break-word;">
                          <div style="height:8px;"> &nbsp; </div>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" vertical-align="middle" class="type-cta" style="font-size:0px;padding:0 0 32px 0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                            <tr>
                              <td align="center" bgcolor="#2e2c35" role="presentation" style="border:none;border-radius:6px;color:white;cursor:auto;padding:14px 24px;" valign="middle"> <a href="{confirm_url}" style="background:#2e2c35;color:white;font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:16px;font-weight:600;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">
                                Confirmar correo
                              </a> </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" style="font-size:0px;word-break:break-word;">
                         <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:14px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #8E8E92;">Este enlace expirará en 1 hora. Nos vemos pronto. Este correo electrónico fue solicitado por {requester_ip}. Si no ha solicitado este correo electrónico, infórmele a livrasand@outlook.com.</div>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size:0px;word-break:break-word;">
                          <div style="height:32px;"> &nbsp; </div>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" style="font-size:0px;padding:24px 16px;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:10px;font-weight:300;line-height:1.2;text-align:center;color:#8E8E92;">© 2024 Kingdom Hall Attendant. Todos los derechos reservados.</div>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </body>

    </html>
    """
    mail.send(msg)

def send_password_email(sender, recipient, password, requester_ip):
    msg = Message('Kingdom Hall Attendant: Recuperación de contraseña', sender=sender, recipients=[recipient])
    msg.html = f"""
    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <title> </title>
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style type="text/css">
        #outlook a {{
          padding: 0;
        }}

        body {{
          margin: 0;
          padding: 0;
          -webkit-text-size-adjust: 100%;
          -ms-text-size-adjust: 100%;
        }}

        table,
        td {{
          border-collapse: collapse;
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
        }}

        img {{
          border: 0;
          height: auto;
          line-height: 100%;
          outline: none;
          text-decoration: none;
          -ms-interpolation-mode: bicubic;
        }}

        p {{
          display: block;
          margin: 13px 0;
        }}
      </style>
      <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
      <![endif]-->
      <!--[if lte mso 11]>
        <style type="text/css">
          .outlook-group-fix {{ width:100% !important; }}
        </style>
      <![endif]-->
      <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
      <style type="text/css">
        @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
      </style>
      <style type="text/css">
        @media only screen and (min-width:480px) {{
          .mj-column-per-100 {{
            width: 100% !important;
            max-width: 100%;
          }}
        }}
      </style>
      <style type="text/css">
        @media only screen and (max-width:480px) {{
          table.full-width-mobile {{
            width: 100% !important;
          }}
          td.full-width-mobile {{
            width: auto !important;
          }}
        }}
      </style>
      <style type="text/css">
        * {{
          text-rendering: optimizeLegibility;
          -moz-osx-font-smoothing: grayscale;
          font-smoothing: antialiased;
          -webkit-font-smoothing: antialiased;
        }}

        .type-cta {{
          user-select: none;
        }}

        .type-nostyle {{
          text-decoration: none;
        }}

        p {{
          margin-top: 0;
        }}
      </style>
    </head>

    <body style="background-color:white;">
      <div style="background-color:white;">
        <!-- logo -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:64px 10% 12px 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:54px;"> <a href="https://www.getkha.org" target="_blank">
                                  <img alt="kingdom hall attendant logo" height="auto" src="https://www.getkha.org/static/images/313010479-cfab1393-8ae1-4b3f-9895-7022272f1262.jpeg" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;border-radius:25%;" width="54"/>
                                </a> </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body head -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:12px 10% 4px 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:8px 0 0 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:22px;font-weight:600;line-height:1.2;text-align:center;color:#000000;">Hola. ¿Se te olvidó tu contraseña?</div>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body content -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="center" style="font-size:0px;padding:16px 16px 0 16px;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:488px;"> <img alt="kingdom hall attendant subscribe loader" height="auto" src="https://assets.dekks.app/mails/marketing/dekks-loader.gif" style="border:0;border-radius:12px;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="488" /> </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- body content -->
        <div style="margin:0px auto;max-width:520px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:12px 10% 0 10%;text-align:center;">
                  <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Tu contraseña es:</span> {password}. Por favor, mantén esta información en un lugar seguro y no compartas tu contraseña con nadie.</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Your password is:</span> {password}. Please keep this information in a safe place and do not share your password with anyone.</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">La tua password è:</span> {password}. Ti preghiamo di conservare queste informazioni in un luogo sicuro e di non condividere la tua password con nessuno.</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Votre mot de passe est :</span> {password}. Veuillez conserver ces informations dans un endroit sûr et ne partagez votre mot de passe avec personne.</div>
                        </td>
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:8px 0 16px 0;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #000000;">Sua senha é:</span> {password}. Por favor, guarde essas informações em um local seguro e não compartilhe sua senha com ninguém.</div>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size:0px;word-break:break-word;">
                          <div style="height:8px;"> &nbsp; </div>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" vertical-align="middle" class="type-cta" style="font-size:0px;padding:0 0 32px 0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                            <tr>
                              <td align="center" bgcolor="#2e2c35" role="presentation" style="border:none;border-radius:6px;color:white;cursor:auto;padding:14px 24px;" valign="middle"> <a href="https://www.getkha.org/login" style="background:#2e2c35;color:white;font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:16px;font-weight:600;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">
                                Iniciar sesión
                              </a> </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" style="font-size:0px;word-break:break-word;">
                         <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:14px;font-weight:600;line-height:1.4;text-align:left;color:#8E8E92;"><span style="color: #8E8E92;">Este correo electrónico fue solicitado por {requester_ip}. Si no ha solicitado este correo electrónico, infórmele a livrasand@outlook.com.</div>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size:0px;word-break:break-word;">
                          <div style="height:32px;"> &nbsp; </div>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" style="font-size:0px;padding:24px 16px;word-break:break-word;">
                          <div style="font-family:-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;font-size:10px;font-weight:300;line-height:1.2;text-align:center;color:#8E8E92;">© 2024 Kingdom Hall Attendant. Todos los derechos reservados.</div>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </body>

    </html>
    """
    mail.send(msg)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html') 

@app.route('/confirm/<token>', methods=['GET', 'POST'])
def confirm_email(token):
    # Crear una conexión directa a cavea.db
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT correo, token_expiration FROM emptor WHERE token = ?", (token,))
    result = cursor.fetchone()
    
    if result:
        email = result['correo']
        token_expiration = result['token_expiration']
        
        # Verificar si el token ha expirado
        if datetime.datetime.now() > datetime.datetime.fromisoformat(token_expiration):
            flash('El enlace de confirmación ha expirado. Por favor, solicita un nuevo enlace.')
            return redirect(url_for('resend_token', email=email))
        
        if request.method == 'POST':
            password = request.form['password']
            
            # Actualizar la entrada en la base de datos con la contraseña y last_login
            now = datetime.datetime.now()
            logging.debug(f"Actualizando last_login a: {now}")
            cursor.execute("UPDATE emptor SET contraseña = ?, last_login = ? WHERE correo = ?", (password, now, email))
            conn.commit()
            conn.close()

            flash('Correo confirmado y contraseña establecida.')
            return redirect(url_for('login'))
        
        conn.close()
        return render_template('confirm.html', token=token)
    else:
        conn.close()
        flash('El enlace de confirmación es inválido o ha expirado.')
        return redirect(url_for('register'))

@app.route('/literatura')
def literatura():
    cursor = g.bd.cursor()

    cursor.execute("SELECT * FROM inventario")
    inventarios = cursor.fetchall()  

    cursor.execute("SELECT nombre_congregacion FROM congregacion")
    congregacion = cursor.fetchone()

    if congregacion and congregacion[0].strip():
        congregacion_formateada = congregacion[0].strip("()'")
    else:
        congregacion_formateada = None 

    return render_template('literatura.html', inventarios=inventarios, congregacion=congregacion_formateada) 

@app.route('/nuevo_inventario')
def nuevo_inventario():
  now = datetime.datetime.now()
  month_year = format_date(now, format='MMMM yyyy', locale='es_ES')

  return render_template('detalle-literatura.html', month_year=month_year, detalle_inventario=None) 

@app.route('/mostrar_inventario/<string:mes_ano>', methods=['GET'])
def mostrar_inventario(mes_ano):
    cursor = g.bd.cursor()

    cursor.execute("SELECT * FROM inventario WHERE mes_ano = ?", (mes_ano,))
    detalle_inventario = cursor.fetchone()

    return render_template('detalle-literatura.html', detalle_inventario=detalle_inventario)

@app.route('/guardar_inventario', methods=['POST'])
def guardar_inventario():
    now = datetime.datetime.now()
    month_year = format_date(now, format='MMMM yyyy', locale='es_ES')

    if request.method == 'POST':     
        mes_ano = month_year
        nwt = request.form['nwt']
        nwtpkt = request.form['nwtpkt']
        otras_biblias = request.form['otras-biblias']
        be = request.form['be']
        cf = request.form['cf']
        cl = request.form['cl']
        ia = request.form['ia']
        jy = request.form['jy']
        kr = request.form['kr']
        lfb = request.form['lfb']
        lff = request.form['lff']
        lr = request.form['lr']
        od = request.form['od']
        rr = request.form['rr']
        scl = request.form['scl']
        sjj = request.form['sjj']
        sjjls = request.form['sjjls']
        sjjyls = request.form['sjjyls']
        yp1 = request.form['yp1']
        yp2 = request.form['yp2']
        otros_libros = request.form['otros-libros']
        ay = request.form['ay']
        ed = request.form['ed']
        hf = request.form['hf']
        hl = request.form['hl']
        la = request.form['la']
        lc = request.form['lc']
        ld = request.form['ld']
        lf = request.form['lf']
        lffi = request.form['lffi']
        ll = request.form['ll']
        lmd = request.form['lmd']
        mb = request.form['mb']
        ol = request.form['ol']
        pc = request.form['pc']
        ph = request.form['ph']
        rj = request.form['rj']
        rk = request.form['rk']
        sp = request.form['sp']
        th = request.form['th']
        wfg = request.form['wfg']
        ypq = request.form['ypq']
        otros_folletos = request.form['otros-folletos']
        inv = request.form['inv']
        t_30 = request.form['t-30']
        t_31 = request.form['t-31']
        t_32 = request.form['t-32']
        t_33 = request.form['t-33']
        t_34 = request.form['t-34']
        t_35 = request.form['t-35']
        t_36 = request.form['t-36']
        t_37 = request.form['t-37']
        jwcd1 = request.form['jwcd1']
        jwcd4 = request.form['jwcd4']
        jwcd9 = request.form['jwcd9']
        jwcd10 = request.form['jwcd10']
        s_34 = request.form['s-34']
        s_24 = request.form['s-24']
        g18_1 = request.form['g18.1']
        g18_2 = request.form['g18.2']
        g18_3 = request.form['g18.3']
        g19_1 = request.form['g19.1']
        g19_2 = request.form['g19.2']
        g19_3 = request.form['g19.3']
        g20_1 = request.form['g20.1']
        g20_2 = request.form['g20.2']
        g20_3 = request.form['g20.3']
        g21_1 = request.form['g21.1']
        g21_2 = request.form['g21.2']
        g21_3 = request.form['g21.3']
        g22_1 = request.form['g22.1']
        g23_1 = request.form['g23.1']
        wp18_1 = request.form['wp18.1']
        wp18_2 = request.form['wp18.2']
        wp18_3 = request.form['wp18.3']
        wp19_1 = request.form['wp19.1']
        wp19_2 = request.form['wp19.2']
        wp19_3 = request.form['wp19.3']
        wp20_1 = request.form['wp20.1']
        wp20_2 = request.form['wp20.2']
        wp20_3 = request.form['wp20.3']
        wp21_1 = request.form['wp21.1']
        wp21_2 = request.form['wp21.2']
        wp21_3 = request.form['wp21.3']
        wp22_1 = request.form['wp22.1']
        wp22_2 = request.form['wp22.2']
        wp22_3 = request.form['wp22.3']
        wp23_1 = request.form['wp23.1']
        wp24_1 = request.form['wp24.1']
        otros_revistas = request.form['otros-revistas']

        cursor = g.bd.cursor()

        # Verificar si ya existe una configuración para este usuario
        cursor.execute("SELECT * FROM inventario WHERE mes_ano = ?", (mes_ano,))
        existing_inventario = cursor.fetchone()

        if existing_inventario:
            # Si ya existe una configuración, actualizarla
            cursor.execute("""
                UPDATE inventario
SET
    mes_ano = ?,
    nwt = ?,
    nwtpkt = ?,
    otras_biblias = ?,
    be = ?,
    cf = ?,
    cl = ?,
    ia = ?,
    jy = ?,
    kr = ?,
    lfb = ?,
    lff = ?,
    lr = ?,
    od = ?,
    rr = ?,
    scl = ?,
    sjj = ?,
    sjjls = ?,
    sjjyls = ?,
    yp1 = ?,
    yp2 = ?,
    otros_libros = ?,
    ay = ?,
    ed = ?,
    hf = ?,
    hl = ?,
    la = ?,
    lc = ?,
    ld = ?,
    lf = ?,
    lffi = ?,
    ll = ?,
    lmd = ?,
    mb = ?,
    ol = ?,
    pc = ?,
    ph = ?,
    rj = ?,
    rk = ?,
    sp = ?,
    th = ?,
    wfg = ?,
    ypq = ?,
    otros_folletos = ?,
    inv = ?,
    t_30 = ?,
    t_31 = ?,
    t_32 = ?,
    t_33 = ?,
    t_34 = ?,
    t_35 = ?,
    t_36 = ?,
    t_37 = ?,
    jwcd1 = ?,
    jwcd4 = ?,
    jwcd9 = ?,
    jwcd10 = ?,
    s_34 = ?,
    s_24 = ?,
    g18_1 = ?,
    g18_2 = ?,
    g18_3 = ?,
    g19_1 = ?,
    g19_2 = ?,
    g19_3 = ?,
    g20_1 = ?,
    g20_2 = ?,
    g20_3 = ?,
    g21_1 = ?,
    g21_2 = ?,
    g21_3 = ?,
    g22_1 = ?,
    g23_1 = ?,
    wp18_1 = ?,
    wp18_2 = ?,
    wp18_3 = ?,
    wp19_1 = ?,
    wp19_2 = ?,
    wp19_3 = ?,
    wp20_1 = ?,
    wp20_2 = ?,
    wp20_3 = ?,
    wp21_1 = ?,
    wp21_2 = ?,
    wp21_3 = ?,
    wp22_1 = ?,
    wp22_2 = ?,
    wp22_3 = ?,
    wp23_1 = ?,
    wp24_1 = ?,
    otros_revistas = ?
WHERE mes_ano = mes_ano

            """, (mes_ano, nwt, nwtpkt, otras_biblias, be, cf, cl, ia, jy, kr, lfb, lff, lr, od, rr, scl, sjj, sjjls, sjjyls, yp1, yp2, 
            otros_libros, ay, ed, hf, hl, la, lc, ld, lf, lffi, ll, lmd, mb, ol, pc, ph, rj, rk, sp, th, wfg, ypq, otros_folletos, 
            inv, t_30, t_31, t_32, t_33, t_34, t_35, t_36, t_37, jwcd1, jwcd4, jwcd9, jwcd10, s_34, s_24, g18_1, g18_2, g18_3, 
            g19_1, g19_2, g19_3, g20_1, g20_2, g20_3, g21_1, g21_2, g21_3, g22_1, g23_1, wp18_1, wp18_2, wp18_3, wp19_1, wp19_2, 
            wp19_3, wp20_1, wp20_2, wp20_3, wp21_1, wp21_2, wp21_3, wp22_1, wp22_2, wp22_3, wp23_1, wp24_1, otros_revistas))
        else:
            # Si no existe una configuración, insertarla
            cursor.execute("""
                INSERT INTO inventario (mes_ano, nwt, nwtpkt, otras_biblias, be, cf, cl, ia, jy, kr, lfb, lff, lr, od, rr, scl, sjj, sjjls, sjjyls, yp1, yp2, 
            otros_libros, ay, ed, hf, hl, la, lc, ld, lf, lffi, ll, lmd, mb, ol, pc, ph, rj, rk, sp, th, wfg, ypq, otros_folletos, 
            inv, t_30, t_31, t_32, t_33, t_34, t_35, t_36, t_37, jwcd1, jwcd4, jwcd9, jwcd10, s_34, s_24, g18_1, g18_2, g18_3, 
            g19_1, g19_2, g19_3, g20_1, g20_2, g20_3, g21_1, g21_2, g21_3, g22_1, g23_1, wp18_1, wp18_2, wp18_3, wp19_1, wp19_2, 
            wp19_3, wp20_1, wp20_2, wp20_3, wp21_1, wp21_2, wp21_3, wp22_1, wp22_2, wp22_3, wp23_1, wp24_1, otros_revistas)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (mes_ano, nwt, nwtpkt, otras_biblias, be, cf, cl, ia, jy, kr, lfb, lff, lr, od, rr, scl, sjj, sjjls, sjjyls, yp1, yp2, 
            otros_libros, ay, ed, hf, hl, la, lc, ld, lf, lffi, ll, lmd, mb, ol, pc, ph, rj, rk, sp, th, wfg, ypq, otros_folletos, 
            inv, t_30, t_31, t_32, t_33, t_34, t_35, t_36, t_37, jwcd1, jwcd4, jwcd9, jwcd10, s_34, s_24, g18_1, g18_2, g18_3, 
            g19_1, g19_2, g19_3, g20_1, g20_2, g20_3, g21_1, g21_2, g21_3, g22_1, g23_1, wp18_1, wp18_2, wp18_3, wp19_1, wp19_2, 
            wp19_3, wp20_1, wp20_2, wp20_3, wp21_1, wp21_2, wp21_3, wp22_1, wp22_2, wp22_3, wp23_1, wp24_1, otros_revistas))
            
        g.bd.commit()

        return redirect('/literatura')    
    
@app.route('/eliminar_inventario/<string:mes_ano>', methods=['GET'])
def eliminar_inventario(mes_ano):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM inventario WHERE mes_ano = ?", (mes_ano,))
    g.bd.commit()
    return redirect('/literatura')

@app.route('/eliminar_vidaministerio/<int:id>', methods=['GET'])
def eliminar_vidaministerio(id):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM vida_ministerio WHERE id = ?", (id,))
    g.bd.commit()
    return redirect('/vida-ministerio.html')

@app.route('/logout')
def logout():
    # Aquí, si estás manejando una conexión específica del usuario, ciérrala.
    user_db_name = session.get('user_db')
    if user_db_name:
        # Cerrar y eliminar la conexión del diccionario
        conn = cursor = get_db().cursor()
        if conn:
            conn.close()

    # Elimina la información de sesión
    session.pop('user_db', None)
    session.pop('user_id', None)
    session.pop('user_ge', None)
    session.pop('language', None)
    # Redirige a la página de inicio o a otra página

    # Verificar si la solicitud proviene de la aplicación de escritorio
    if request.headers.get('X-Client-Type') == 'desktop':
        return redirect(url_for('login_desktop'))
    return redirect('/')
        
if __name__ == '__main__':
    app.run(debug=True)