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

if __name__ == '__main__':
    app.run(debug=True)
