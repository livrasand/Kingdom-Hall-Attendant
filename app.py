from flask import Flask, render_template, request, redirect, g
import sqlite3

app = Flask(__name__)

# Función para conectar a la base de datos
def conectar_bd():
    return sqlite3.connect('kha.db')

# Antes de cada solicitud, se abre la conexión a la base de datos
@app.before_request
def antes_de_la_peticion():
    g.bd = conectar_bd()

# Después de cada solicitud, se cierra la conexión a la base de datos
@app.teardown_request
def despues_de_la_peticion(excepcion):
    if hasattr(g, 'bd'):
        g.bd.close()

# Ruta para mostrar el formulario y los datos guardados
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/congregacion.html')
def option_one():
     # Obtener los datos de la congregación desde la base de datos
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM congregacion WHERE id = ?", (1,))  # Aquí asumo que la congregación que quieres mostrar tiene el ID 1, cambia esto según tu necesidad
    congregation_data = cursor.fetchone()

    # Pasar los datos de la congregación al template
    return render_template('congregacion.html', congregation=congregation_data)

@app.route('/guardar_congregacion', methods=['POST'])
def guardar_congregacion():
    if request.method == 'POST':
        nombre_congregacion = request.form['nombre_congregacion']
        numero = request.form['numero']
        hora_inicio_semana = request.form['hora_inicio_semana']
        hora_inicio_fin_semana = request.form['hora_inicio_fin_semana']
        direccion_salon = request.form['direccion_salon']
        superintendente_circuito = request.form['superintendente_circuito']
        telefono = request.form['telefono']
        circuito = request.form['circuito']

        # Obtener las opciones seleccionadas de los días de la semana
        opcion_semana = request.form.get('options')
        opcion_fin_semana = request.form.get('optionstwo')

        # Verificar si ya existe un registro para la congregación
        cursor = g.bd.cursor()
        cursor.execute("SELECT * FROM congregacion WHERE nombre_congregacion = ?", (nombre_congregacion,))
        existing_congregation = cursor.fetchone()

        if existing_congregation:
            # Si la congregación ya existe, ejecutar una actualización
            g.bd.execute("UPDATE congregacion SET numero=?, hora_inicio_semana=?, hora_inicio_fin_semana=?, direccion_salon=?, superintendente_circuito=?, telefono=?, circuito=?, opcion_semana=?, opcion_fin_semana=? WHERE nombre_congregacion=?",
                          (numero, hora_inicio_semana, hora_inicio_fin_semana, direccion_salon, superintendente_circuito, telefono, circuito, opcion_semana, opcion_fin_semana, nombre_congregacion))
        else:
            # Si la congregación no existe, ejecutar una inserción
            g.bd.execute("INSERT INTO congregacion (nombre_congregacion, numero, hora_inicio_semana, hora_inicio_fin_semana, direccion_salon, superintendente_circuito, telefono, circuito, opcion_semana, opcion_fin_semana) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (nombre_congregacion, numero, hora_inicio_semana, hora_inicio_fin_semana, direccion_salon, superintendente_circuito, telefono, circuito, opcion_semana, opcion_fin_semana))

        # Guardar los cambios
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
    familias = cursor.fetchall()
    cursor.execute("SELECT * FROM grupos_predicacion")
    grupos_predicacion = cursor.fetchall()
    return render_template('detalle-publicador.html', publicador=None, familias=familias, grupos_predicacion=grupos_predicacion)


@app.route('/mostrar_publicador/<int:id>', methods=['GET'])
def mostrar_publicador(id):
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM publicadores WHERE id = ?", (id,))
    publicador = cursor.fetchone()

    apellidos = publicador[2]

    cursor.execute("SELECT * FROM grupos_predicacion")
    grupos_predicacion = cursor.fetchall()

    # Verificar si ya existe una familia con los apellidos proporcionados
    cursor.execute("SELECT * FROM familias WHERE apellidos_familia = ?", (apellidos,))
    familia_existente = cursor.fetchone() is not None
    return render_template('detalle-publicador.html', publicador=publicador, familia_existente=familia_existente, grupos_predicacion=grupos_predicacion)


# Ruta para guardar los datos de los publicadores
@app.route('/guardar_publicador', methods=['POST'])
def guardar_publicador():
    if request.method == 'POST':
        id = request.form['id']  # Obtener el ID del publicador a editar desde el formulario
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        genero = request.form['genero']
        cabeza_de_familia = 'cabeza_de_familia' in request.form  # Verificar si es cabeza de familia
        fecha_nacimiento = request.form['fecha_nacimiento']
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

        # Convertir valores booleanos a enteros
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

        # Verificar si ya existe un registro para el publicador
        cursor = g.bd.cursor()
        cursor.execute("SELECT * FROM publicadores WHERE nombres = ? AND apellidos = ?", (nombres, apellidos))
        existing_publicador = cursor.fetchone()

        if existing_publicador:
            # Si el publicador existe, ejecutar una actualización
            g.bd.execute("UPDATE publicadores SET nombres=?, apellidos=?, genero=?, cabeza_de_familia=?, fecha_nacimiento=?, direccion=?, correo_electronico=?, celular=?, telefono=?, bautizado=?, fecha_bautizo=?, recibe_atalaya=?, recibe_guia_actividades=?, no_bautizado=?, temporal=?, ungido=?, nino=?, readmitido=?, irregular=?, invidente=?, abuso_sexual=?, divorciado=?, viudo=?, sordo=?, enfermo=?, voluntario_ldc=?, voluntario_epc=?, llaves_salon=?, utiliza_kha=?, censurado=?, inactivo=?, expulsado=?, fallecido=?, encarcelado=?, separado=?, nombramientos=?, fecha_inicio_nombrado=?, privilegios_servicio=?, fecha_inicio=?, numero_precursor=?, temporario=?, enfermizo=?, fecha_ultima_escuela=?, checkbox_coordinador_cuerpo_ancianos=?, checkbox_secretario=?, checkbox_superintendente_servicio=?, checkbox_siervo_acomodadores=?, checkbox_coordinador_audio_video=?, checkbox_siervo_literatura=?, checkbox_coordinador_mantenimiento=?, checkbox_coordinador_mantenimiento_jardin=?, checkbox_comite_mantenimiento_salon_reino=?, checkbox_consejero_sala_auxiliar=?, checkbox_consejero_auxiliar=?, checkbox_voluntario_temporal_betel=?, checkbox_betelita_cercanias=?, checkbox_voluntario_remoto_betel=?, checkbox_comite_enlace_hospitalario=?, checkbox_conductor_estudio_atalaya=?, checkbox_coordinador_discursos_publicos=?, checkbox_ayudante_coordinador_discursos_publicos=?, checkbox_siervo_informes=?, checkbox_siervo_cuentas=?, checkbox_siervo_territorios=?, checkbox_coordinador_limpieza=?, checkbox_superintendente_reunion_vida_ministerio_cristianos=?, checkbox_coordinador_predicacion_publica=?, checkbox_superintendente_grupo=?, checkbox_siervo_grupo=?, checkbox_auxiliar_grupo=?, checkbox_betelita=?, checkbox_voluntario_construccion=?, checkbox_siervo_construccion=?, checkbox_presidente=?, checkbox_oracion=?, checkbox_discurso_10_mins=?, checkbox_busquemos_perlas_escondidas=?, checkbox_lectura_biblia=?, checkbox_analisis=?, checkbox_empiece_conversaciones=?, checkbox_haga_revisitas=?, checkbox_haga_discipulos=?, checkbox_no_utilizar_sala_principal=?, checkbox_explique_sus_creencias=?, checkbox_ayudante=?, checkbox_discurso=?, checkbox_utilizar_solo_sala_principal=?, checkbox_intervenciones=?, checkbox_estudio_biblico_congregacion=?, checkbox_lector=?, checkbox_discursante_publico_saliente=?, checkbox_discursante_publico_local=?, checkbox_presidente_reunion_publica=?, checkbox_lector_atalaya=?, checkbox_anfitrion_hospitalidades=?, checkbox_operador_audio=?, checkbox_plataforma=?, checkbox_anfitrion_zoom=?, checkbox_microfonos=?, checkbox_coanfitrion_zoom=?, checkbox_acomodador=?, checkbox_aprobado_predicacion_publica=?, checkbox_dirigir_reuniones_servicio_campo=?, checkbox_orar_reuniones_servicio_campo=?, checkbox_limpieza_semanal_salon_reino=?, checkbox_limpieza_despues_reunion=?, checkbox_cuidado_jardin=?, checkbox_limpieza_mensual_salon_reino=?, checkbox_limpieza_trimestral_salon_reino=?, checkbox_cuidado_cesped=? WHERE id=?",
                (nombres, apellidos, genero, cabeza_de_familia, fecha_nacimiento, direccion, correo_electronico, celular, telefono, bautizado, fecha_bautizo, recibe_atalaya, recibe_guia_actividades, no_bautizado, temporal, ungido, nino, readmitido, irregular, invidente, abuso_sexual, divorciado, viudo, sordo, enfermo, voluntario_ldc, voluntario_epc, llaves_salon, utiliza_kha, censurado, inactivo, expulsado, fallecido, encarcelado, separado, nombramientos, fecha_inicio_nombrado, privilegios_servicio, fecha_inicio, numero_precursor, temporario, enfermizo, fecha_ultima_escuela, checkbox_coordinador_cuerpo_ancianos, checkbox_secretario, checkbox_superintendente_servicio, checkbox_siervo_acomodadores, checkbox_coordinador_audio_video, checkbox_siervo_literatura, checkbox_coordinador_mantenimiento, checkbox_coordinador_mantenimiento_jardin, checkbox_comite_mantenimiento_salon_reino, checkbox_consejero_sala_auxiliar, checkbox_consejero_auxiliar, checkbox_voluntario_temporal_betel, checkbox_betelita_cercanias, checkbox_voluntario_remoto_betel, checkbox_comite_enlace_hospitalario, checkbox_conductor_estudio_atalaya, checkbox_coordinador_discursos_publicos, checkbox_ayudante_coordinador_discursos_publicos, checkbox_siervo_informes, checkbox_siervo_cuentas, checkbox_siervo_territorios, checkbox_coordinador_limpieza, checkbox_superintendente_reunion_vida_ministerio_cristianos, checkbox_coordinador_predicacion_publica, checkbox_superintendente_grupo, checkbox_siervo_grupo, checkbox_auxiliar_grupo, checkbox_betelita, checkbox_voluntario_construccion, checkbox_siervo_construccion, checkbox_presidente, checkbox_oracion, checkbox_discurso_10_mins, checkbox_busquemos_perlas_escondidas, checkbox_lectura_biblia, checkbox_analisis, checkbox_empiece_conversaciones, checkbox_haga_revisitas, checkbox_haga_discipulos, checkbox_no_utilizar_sala_principal, checkbox_explique_sus_creencias, checkbox_ayudante, checkbox_discurso, checkbox_utilizar_solo_sala_principal, checkbox_intervenciones, checkbox_estudio_biblico_congregacion, checkbox_lector, checkbox_discursante_publico_saliente, checkbox_discursante_publico_local, checkbox_presidente_reunion_publica, checkbox_lector_atalaya, checkbox_anfitrion_hospitalidades, checkbox_operador_audio, checkbox_plataforma, checkbox_anfitrion_zoom, checkbox_microfonos, checkbox_coanfitrion_zoom, checkbox_acomodador, checkbox_aprobado_predicacion_publica, checkbox_dirigir_reuniones_servicio_campo, checkbox_orar_reuniones_servicio_campo, checkbox_limpieza_semanal_salon_reino, checkbox_limpieza_despues_reunion, checkbox_cuidado_jardin, checkbox_limpieza_mensual_salon_reino, checkbox_limpieza_trimestral_salon_reino, checkbox_cuidado_cesped, existing_publicador[0]))
        else:
            g.bd.execute("INSERT INTO publicadores (nombres, apellidos, genero, cabeza_de_familia, fecha_nacimiento, direccion, correo_electronico, celular, telefono, bautizado, fecha_bautizo, recibe_atalaya, recibe_guia_actividades, no_bautizado, temporal, ungido, nino, readmitido, irregular, invidente, abuso_sexual, divorciado, viudo, sordo, enfermo, voluntario_ldc, voluntario_epc, llaves_salon, utiliza_kha, censurado, inactivo, expulsado, fallecido, encarcelado, separado, nombramientos, fecha_inicio_nombrado, privilegios_servicio, fecha_inicio, numero_precursor, temporario, enfermizo, fecha_ultima_escuela, checkbox_coordinador_cuerpo_ancianos, checkbox_secretario, checkbox_superintendente_servicio, checkbox_siervo_acomodadores, checkbox_coordinador_audio_video, checkbox_siervo_literatura, checkbox_coordinador_mantenimiento, checkbox_coordinador_mantenimiento_jardin, checkbox_comite_mantenimiento_salon_reino, checkbox_consejero_sala_auxiliar, checkbox_consejero_auxiliar, checkbox_voluntario_temporal_betel, checkbox_betelita_cercanias, checkbox_voluntario_remoto_betel, checkbox_comite_enlace_hospitalario, checkbox_conductor_estudio_atalaya, checkbox_coordinador_discursos_publicos, checkbox_ayudante_coordinador_discursos_publicos, checkbox_siervo_informes, checkbox_siervo_cuentas, checkbox_siervo_territorios, checkbox_coordinador_limpieza, checkbox_superintendente_reunion_vida_ministerio_cristianos, checkbox_coordinador_predicacion_publica, checkbox_superintendente_grupo, checkbox_siervo_grupo, checkbox_auxiliar_grupo, checkbox_betelita, checkbox_voluntario_construccion, checkbox_siervo_construccion, checkbox_presidente, checkbox_oracion, checkbox_discurso_10_mins, checkbox_busquemos_perlas_escondidas, checkbox_lectura_biblia, checkbox_analisis, checkbox_empiece_conversaciones, checkbox_haga_revisitas, checkbox_haga_discipulos, checkbox_no_utilizar_sala_principal, checkbox_explique_sus_creencias, checkbox_ayudante, checkbox_discurso, checkbox_utilizar_solo_sala_principal, checkbox_intervenciones, checkbox_estudio_biblico_congregacion, checkbox_lector, checkbox_discursante_publico_saliente, checkbox_discursante_publico_local, checkbox_presidente_reunion_publica, checkbox_lector_atalaya, checkbox_anfitrion_hospitalidades, checkbox_operador_audio, checkbox_plataforma, checkbox_anfitrion_zoom, checkbox_microfonos, checkbox_coanfitrion_zoom, checkbox_acomodador, checkbox_aprobado_predicacion_publica, checkbox_dirigir_reuniones_servicio_campo, checkbox_orar_reuniones_servicio_campo, checkbox_limpieza_semanal_salon_reino, checkbox_limpieza_despues_reunion, checkbox_cuidado_jardin, checkbox_limpieza_mensual_salon_reino, checkbox_limpieza_trimestral_salon_reino, checkbox_cuidado_cesped) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (nombres, apellidos, genero, cabeza_de_familia, fecha_nacimiento, direccion, correo_electronico, celular, telefono, bautizado, fecha_bautizo, recibe_atalaya, recibe_guia_actividades, no_bautizado, temporal, ungido, nino, readmitido, irregular, invidente, abuso_sexual, divorciado, viudo, sordo, enfermo, voluntario_ldc, voluntario_epc, llaves_salon, utiliza_kha, censurado, inactivo, expulsado, fallecido, encarcelado, separado, nombramientos, fecha_inicio_nombrado, privilegios_servicio, fecha_inicio, numero_precursor, temporario, enfermizo, fecha_ultima_escuela, checkbox_coordinador_cuerpo_ancianos, checkbox_secretario, checkbox_superintendente_servicio, checkbox_siervo_acomodadores, checkbox_coordinador_audio_video, checkbox_siervo_literatura, checkbox_coordinador_mantenimiento, checkbox_coordinador_mantenimiento_jardin, checkbox_comite_mantenimiento_salon_reino, checkbox_consejero_sala_auxiliar, checkbox_consejero_auxiliar, checkbox_voluntario_temporal_betel, checkbox_betelita_cercanias, checkbox_voluntario_remoto_betel, checkbox_comite_enlace_hospitalario, checkbox_conductor_estudio_atalaya, checkbox_coordinador_discursos_publicos, checkbox_ayudante_coordinador_discursos_publicos, checkbox_siervo_informes, checkbox_siervo_cuentas, checkbox_siervo_territorios, checkbox_coordinador_limpieza, checkbox_superintendente_reunion_vida_ministerio_cristianos, checkbox_coordinador_predicacion_publica, checkbox_superintendente_grupo, checkbox_siervo_grupo, checkbox_auxiliar_grupo, checkbox_betelita, checkbox_voluntario_construccion, checkbox_siervo_construccion, checkbox_presidente, checkbox_oracion, checkbox_discurso_10_mins, checkbox_busquemos_perlas_escondidas, checkbox_lectura_biblia, checkbox_analisis, checkbox_empiece_conversaciones, checkbox_haga_revisitas, checkbox_haga_discipulos, checkbox_no_utilizar_sala_principal, checkbox_explique_sus_creencias, checkbox_ayudante, checkbox_discurso, checkbox_utilizar_solo_sala_principal, checkbox_intervenciones, checkbox_estudio_biblico_congregacion, checkbox_lector, checkbox_discursante_publico_saliente, checkbox_discursante_publico_local, checkbox_presidente_reunion_publica, checkbox_lector_atalaya, checkbox_anfitrion_hospitalidades, checkbox_operador_audio, checkbox_plataforma, checkbox_anfitrion_zoom, checkbox_microfonos, checkbox_coanfitrion_zoom, checkbox_acomodador, checkbox_aprobado_predicacion_publica, checkbox_dirigir_reuniones_servicio_campo, checkbox_orar_reuniones_servicio_campo, checkbox_limpieza_semanal_salon_reino, checkbox_limpieza_despues_reunion, checkbox_cuidado_jardin, checkbox_limpieza_mensual_salon_reino, checkbox_limpieza_trimestral_salon_reino, checkbox_cuidado_cesped))
        
            # Guardar los cambios
            g.bd.commit()

            # Si es cabeza de familia, guardar información adicional de la familia
            if cabeza_de_familia:
                # Aquí puedes manejar la lógica para guardar información adicional de la familia
                # Por ejemplo, mostrar un formulario adicional para ingresar información sobre la familia y guardarlo en la base de datos
                pass

    # Redirigir a la página de publicadores
    return redirect('/publicadores.html')

@app.route('/eliminar_publicador/<int:id>', methods=['GET'])
def eliminar_publicador(id):
    cursor = g.bd.cursor()
    cursor.execute("DELETE FROM publicadores WHERE id = ?", (id,))
    g.bd.commit()
    return redirect('/publicadores.html')

@app.route('/configuracion.html')
def configuracion():
    # Obtener los datos de configuración desde la base de datos
    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM configuracion WHERE id = ?", (1,))
    configuracion_data = cursor.fetchone()

    # Pasar los datos de configuración al template
    return render_template('configuracion.html', configuracion=configuracion_data)

@app.route('/guardar_configuracion', methods=['POST'])
def guardar_configuracion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        user_email = request.form['user_email']
        privilegio = request.form['privilegio']
        pais = request.form['pais']
        congregacion = request.form['congregacion']
        circuito = request.form['circuito']

        
        # Conexión a la base de datos    
        cursor = g.bd.cursor()

        # Ejecutar consulta para insertar o actualizar los datos en la tabla "configuracion"
        cursor.execute("""
            INSERT INTO configuracion (nombre, apellidos, user_email, privilegio, pais, congregacion, circuito)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(user_email) DO UPDATE SET
            nombre = excluded.nombre,
            apellidos = excluded.apellidos,
            privilegio = excluded.privilegio,
            pais = excluded.pais,
            congregacion = excluded.congregacion,
            circuito = excluded.circuito
        """, (nombre, apellidos, user_email, privilegio, pais, congregacion, circuito))
            

        # Guardar los cambios en la base de datos
        g.bd.commit()        

    return redirect('/configuracion.html')

@app.route('/grupos-predicacion.html')
def grupos_predicacion():

    cursor = g.bd.cursor()
    cursor.execute("SELECT * FROM grupos_predicacion")
    grupos = cursor.fetchall()

    return render_template('grupos-predicacion.html', grupos=grupos)

@app.route('/nuevo_grupo', methods=['GET'])
def nuevo_grupo():
    cursor = g.bd.cursor()

    # Consultar los publicadores que tienen checkbox_siervo_grupo en 1
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
    return render_template('detalle-grupo-predicacion.html', grupo=grupo)

# Ruta para guardar los datos del grupo de predicación
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

        # Conexión a la base de datos
        cursor = g.bd.cursor()

        # Ejecutar consulta para insertar los datos en la tabla "grupos_predicacion"
        cursor.execute("""
            INSERT INTO grupos_predicacion (nombre_grupo, siervo_grupo, auxiliar_grupo, direccion_grupo, asignar_hospitalidad, limpieza_salon, reunion_superintendente)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre_grupo, siervo_grupo, auxiliar_grupo, direccion_grupo, asignar_hospitalidad, limpieza_salon, reunion_superintendente))

        # Guardar los cambios en la base de datos
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
        # Insertar los apellidos de la familia en la base de datos
        cursor = g.bd.cursor()

        # Verificar si ya existe una familia con los apellidos proporcionados
        cursor.execute("SELECT * FROM familias WHERE apellidos_familia = ?", (apellidos,))
        familia_existente = cursor.fetchone()

        if not familia_existente:
            # No existe la familia, por lo tanto, puedes crearla
            cursor.execute("INSERT INTO familias (apellidos_familia) VALUES (?)", (apellidos,))
            g.bd.commit()

        return redirect('/publicadores.html')

@app.route('/bosquejos.html')
def bosquejos():
    return render_template('bosquejos.html')

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

        # Repetir para discurso_4 hasta discurso_25
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
    g.bd.commit()
    return redirect('/')

@app.route('/nuevo_orador')
def nuevo_orador():
    return render_template('detalle-orador.html', orador=None)

@app.route('/')
def oradores_foraneos():
    return render_template('')

if __name__ == '__main__':
    app.run(debug=True)
