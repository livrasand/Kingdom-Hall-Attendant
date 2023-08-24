DROP INDEX publicadores_id_idx;

DROP TABLE publicadores;

CREATE TABLE publicadores (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nombre TEXT,
	apellidos TEXT,
	p_email TEXT,
	p_celular TEXT,
	p_telefono INTEGER	
    sexo TEXT,
    cabeza TEXT,
   fecha_nacimiento TEXT,
   direccion TEXT,
   bautizado TEXT,
   p_fecha_bautismo TEXT,
   p_grupo TEXT,
   privilegios_servicio TEXT,
   nombramiento TEXT,
   aprobado_predicacion TEXT,
   orar_servicio_campo TEXT,
   presidente_tb TEXT,
   oracion_tb TEXT,
   discurso_10_tb TEXT,
   busquemos_perlas_tb TEXT,
   consejero_sala_aux_tb TEXT,
   lectura_biblia_tb TEXT,
   discusion_video_sm TEXT,
   primera_conversacion_sm TEXT,
   revisita_sm TEXT,
   no_utilizar_sala_principal_sm TEXT,
   curso_biblico_sm TEXT,
   ayudante_sm TEXT,
   discurso_5_sm TEXT,
   utilizar_sala_principal_sm TEXT,
   intervenciones_nvc TEXT,
   estudio_biblico_nvc TEXT,
   lector_nvc TEXT,
   discursante_publico_le_at TEXT,
   presidente_reunion_publica_le_at TEXT,
   lector_le_at TEXT,
   anfitrion_hospitalidades_le_at TEXT,
   sonido_tareas TEXT,
   plataforma_tareas TEXT,
   anfitrion_zoom_tareas TEXT,
   mantenimiento_tareas TEXT,
   microfonos_tareas TEXT,
   coanfitrion_zoom_tareas TEXT,
   acomodador_tareas TEXT,
   aprobado_predicacion_servicio_campo TEXT,
   dirigir_reuniones_servicio_campo TEXT,
   orar_reuniones_servicio_campo TEXT,
   limpieza_semanal_salon TEXT,
   limpieza_despues_reunion TEXT,
   cuidado_jardin TEXT,
   limpieza_mensual_salon TEXT,
   limpieza_trimestral_salon TEXT,
   cuidado_cesped TEXT
);

CREATE UNIQUE INDEX IF NOT EXISTS publicadores_id_idx ON publicadores (
    id 
);