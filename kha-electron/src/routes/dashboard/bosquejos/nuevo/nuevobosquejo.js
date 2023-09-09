let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) {
    throw new Error(err.message);
  }
  console.log('Connected to the database.');
});

async function cargarOradores() {
    console.log('Cargando lista de oradores desde la base de datos...');
    return new Promise((resolve, reject) => {
      const sql = `
        SELECT id, nombre, apellidos
        FROM oradorespublicos
        UNION
        SELECT id, nombre, apellidos
        FROM oradorespublicosforaneos
      `;
      
      db.all(sql, [], (err, rows) => {
        if (err) {
          console.error('Error al cargar la lista de oradores:', err.message);
          reject(err);
        } else {
          console.log('Lista de oradores cargada:', rows);
          // Eliminar duplicados en función del id
          const uniqueOradores = Array.from(new Set(rows.map((row) => row.id))).map((id) => {
            return rows.find((row) => row.id === id);
          });
          resolve(uniqueOradores);
        }
      });
    });
  }
  
// Modificar la función save para utilizar la lista de oradores cargada
async function save(form) {
  console.log('Guardando datos en la base de datos:', form);
  const {
    id,
    fechaImpartido,
    orador,
    anotaciones,
    haHospitalidad,
    haPresentadoTiempo,
    haPresentadoDiscurso
  } = form;

  const oradores = await cargarOradores();

  // Validar que el ID del orador sea válido
  if (oradores.some((o) => o.id === orador)) {
    const existingData = await new Promise((resolve, reject) => {
      db.get('SELECT * FROM bosquejos WHERE id = ?', [id], (err, row) => {
        if (err) {
          reject(err);
        } else {
          resolve(row);
        }
      });
    });

    if (existingData) {
      const updateSql = `
        UPDATE bosquejos SET
        id = ?,
        fechaImpartido = ?,
        orador = ?,
        anotaciones = ?,
        haHospitalidad = ?,
        haPresentadoTiempo = ?,
        haPresentadoDiscurso = ?
        WHERE id = ?
      `;

      await db.serialize(async () => {
        await db.run('BEGIN TRANSACTION');
        await db.run(updateSql, [
          id,
          fechaImpartido,
          orador,
          anotaciones,
          haHospitalidad,
          haPresentadoTiempo,
          haPresentadoDiscurso,
          id  // Agrega el ID aquí para la cláusula WHERE
        ], (_err) => {
          if (_err) {
            console.error('Error al actualizar datos:', _err.message);
            db.run('ROLLBACK');
          } else {
            console.log('Datos actualizados con éxito.');
            db.run('COMMIT');
          }
        });
      });
    } else {
      // Si no existe un registro existente, realiza una inserción
      console.log('Insertando nuevos datos...');
      const insertSql = `
        INSERT INTO bosquejos
        (id, 
          fechaImpartido,
          orador,
          anotaciones,
          haHospitalidad,
          haPresentadoTiempo,
          haPresentadoDiscurso)
        VALUES (?, ?, ?, ?, ?, ?, ?)
      `;

      await db.serialize(async () => {
        await db.run('BEGIN TRANSACTION');
        await db.run(insertSql, [
          id,
          fechaImpartido,
          orador,
          anotaciones,
          haHospitalidad,
          haPresentadoTiempo,
          haPresentadoDiscurso
        ], (_err) => {
          if (_err) {
            console.error('Error al insertar datos:', _err.message);
            db.run('ROLLBACK');
          } else {
            console.log('Datos insertados con éxito.');
            db.run('COMMIT');
          }
        });
      });
    }
  } else {
    console.error('ID de orador no válido.');
  }
}

// Función para cargar datos desde la base de datos
async function load() {
  console.log('Fetching data from the database...');
  return new Promise((resolve, reject) => {
    sql = `SELECT * FROM bosquejos`;
    db.all(sql, [], (err, rows) => {
      if (err) {
        console.error('Error fetching data:', err.message);
        reject(err);
      } else {
        console.log('Data fetched:', rows);
        resolve(rows);
      }
    });
  });
}

export { load, save, cargarOradores };
