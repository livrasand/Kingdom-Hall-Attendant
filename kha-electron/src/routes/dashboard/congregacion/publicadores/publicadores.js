let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) {
    throw new Error(err.message);
  }
});

async function load() {
  return new Promise((resolve, reject) => {
    sql = `select * from publicadores`;
    db.all(sql, [], (err, rows) => {
      if (err) {
        console.error(err.message);
      }
      resolve(rows);
    });
  });
}

function loadById(id) {
  return new Promise((resolve, reject) => {
    const sql = 'SELECT * FROM publicadores WHERE id = ?';
    db.get(sql, [id], (err, row) => {
      if (err) {
        console.error(err.message);
        reject(err);
      }
      resolve(row);
    });
  });
}

async function save(form) {
  const {
    id,
    nombre, 
    apellidos,
    sexo,
    cabeza,
   fecha_nacimiento,
   direccion,
   p_email,
   p_celular,
   p_telefono,
   bautizado,
   p_fecha_bautismo,
   p_grupo,
   privilegios_servicio,
   nombramiento,
   aprobado_predicacion,
   orar_servicio_campo,
   presidente_tb,
   oracion_tb,
   discurso_10_tb,
   busquemos_perlas_tb,
   consejero_sala_aux_tb,
   lectura_biblia_tb,
   discusion_video_sm,
   primera_conversacion_sm,
   revisita_sm,
   no_utilizar_sala_principal_sm,
   curso_biblico_sm,
   ayudante_sm,
   discurso_5_sm,
   utilizar_sala_principal_sm,
   intervenciones_nvc,
   estudio_biblico_nvc,
   lector_nvc,
   discursante_publico_le_at,
   presidente_reunion_publica_le_at,
   lector_le_at,
   anfitrion_hospitalidades_le_at,
   sonido_tareas,
   plataforma_tareas,
   anfitrion_zoom_tareas,
   mantenimiento_tareas,
   microfonos_tareas,
   coanfitrion_zoom_tareas,
   acomodador_tareas,
   aprobado_predicacion_servicio_campo,
   dirigir_reuniones_servicio_campo,
   orar_reuniones_servicio_campo,
   limpieza_semanal_salon,
   limpieza_despues_reunion,
   cuidado_jardin,
   limpieza_mensual_salon,
   limpieza_trimestral_salon,
   cuidado_cesped
  } = form;

  const existingData = await new Promise((resolve, reject) => {
    db.get('SELECT * FROM publicadores WHERE id = ?', [id], (err, row) => {
      if (err) {
        reject(err);
      } else {
        resolve(row);
      }
    });
  });

  if (existingData) {
    sql = `
      UPDATE publicadores SET
      nombre = ?,
      apellidos = ?,
      sexo = ?,
      cabeza = ?,
      fecha_nacimiento = ?,
      direccion = ?,
      p_email = ?,
      p_celular = ?,
      p_telefono = ?,
      bautizado = ?,
      p_fecha_bautismo = ?,
      p_grupo = ?,
      privilegios_servicio = ?,
      nombramiento = ?,
      aprobado_predicacion = ?,
      orar_servicio_campo = ?,
      presidente_tb = ?,
      oracion_tb = ?,
      discurso_10_tb = ?,
      busquemos_perlas_tb = ?,
      consejero_sala_aux_tb = ?,
      lectura_biblia_tb = ?,
      discusion_video_sm = ?,
      primera_conversacion_sm = ?,
      revisita_sm = ?,
      no_utilizar_sala_principal_sm = ?,
      curso_biblico_sm = ?,
      ayudante_sm = ?,
      discurso_5_sm = ?,
      utilizar_sala_principal_sm = ?,
      intervenciones_nvc = ?,
      estudio_biblico_nvc = ?,
      lector_nvc = ?,
      discursante_publico_le_at = ?,
      presidente_reunion_publica_le_at = ?,
      lector_le_at = ?,
      anfitrion_hospitalidades_le_at = ?,
      sonido_tareas = ?,
      plataforma_tareas = ?,
      anfitrion_zoom_tareas = ?,
      mantenimiento_tareas = ?,
      microfonos_tareas = ?,
      coanfitrion_zoom_tareas = ?,
      acomodador_tareas = ?,
      aprobado_predicacion_servicio_campo = ?,
      dirigir_reuniones_servicio_campo = ?,
      orar_reuniones_servicio_campo = ?,
      limpieza_semanal_salon = ?,
      limpieza_despues_reunion = ?,
      cuidado_jardin = ?,
      limpieza_mensual_salon = ?,
      limpieza_trimestral_salon = ?,
      cuidado_cesped = ?
      WHERE id = ?
    `;
  } else {
    sql = `
      INSERT OR REPLACE INTO publicadores (
        id,
        nombre,
        apellidos,
        sexo,
        cabeza,
        fecha_nacimiento,
        direccion,
        p_email,
        p_celular,
        p_telefono,
        bautizado,
        p_fecha_bautismo,
        p_grupo,
        privilegios_servicio,
        nombramiento,
        aprobado_predicacion,
        orar_servicio_campo,
        presidente_tb,
        oracion_tb,
        discurso_10_tb,
        busquemos_perlas_tb,
        consejero_sala_aux_tb,
        lectura_biblia_tb,
        discusion_video_sm,
        primera_conversacion_sm,
        revisita_sm,
        no_utilizar_sala_principal_sm,
        curso_biblico_sm,
        ayudante_sm,
        discurso_5_sm,
        utilizar_sala_principal_sm,
        intervenciones_nvc,
        estudio_biblico_nvc,
        lector_nvc,
        discursante_publico_le_at,
        presidente_reunion_publica_le_at,
        lector_le_at,
        anfitrion_hospitalidades_le_at,
        sonido_tareas,
        plataforma_tareas,
        anfitrion_zoom_tareas,
        mantenimiento_tareas,
        microfonos_tareas,
        coanfitrion_zoom_tareas,
        acomodador_tareas,
        aprobado_predicacion_servicio_campo,
        dirigir_reuniones_servicio_campo,
        orar_reuniones_servicio_campo,
        limpieza_semanal_salon,
        limpieza_despues_reunion,
        cuidado_jardin,
        limpieza_mensual_salon,
        limpieza_trimestral_salon,
        cuidado_cesped
      ) values (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
      )
    `;
  }

  await db.serialize(async () => {
    await db.run('BEGIN TRANSACTION');
    await db.run(sql, [
      id,
      nombre,
      apellidos,
      sexo,
      cabeza,
      fecha_nacimiento,
      direccion,
      p_email,
      p_celular,
      p_telefono,
      bautizado,
      p_fecha_bautismo,
      p_grupo,
      privilegios_servicio,
      nombramiento,
      aprobado_predicacion,
      orar_servicio_campo,
      presidente_tb,
      oracion_tb,
      discurso_10_tb,
      busquemos_perlas_tb,
      consejero_sala_aux_tb,
      lectura_biblia_tb,
      discusion_video_sm,
      primera_conversacion_sm,
      revisita_sm,
      no_utilizar_sala_principal_sm,
      curso_biblico_sm,
      ayudante_sm,
      discurso_5_sm,
      utilizar_sala_principal_sm,
      intervenciones_nvc,
      estudio_biblico_nvc,
      lector_nvc,
      discursante_publico_le_at,
      presidente_reunion_publica_le_at,
      lector_le_at,
      anfitrion_hospitalidades_le_at,
      sonido_tareas,
      plataforma_tareas,
      anfitrion_zoom_tareas,
      mantenimiento_tareas,
      microfonos_tareas,
      coanfitrion_zoom_tareas,
      acomodador_tareas,
      aprobado_predicacion_servicio_campo,
      dirigir_reuniones_servicio_campo,
      orar_reuniones_servicio_campo,
      limpieza_semanal_salon,
      limpieza_despues_reunion,
      cuidado_jardin,
      limpieza_mensual_salon,
      limpieza_trimestral_salon,
      cuidado_cesped
    ], (_err) => {
      if (_err) {
        console.log(_err.message);
        db.run('ROLLBACK');
      } else {
        alert(`Registro actualizado`);
        db.run('COMMIT');
      }
    })
    }
  )
}

export {load, loadById, save};