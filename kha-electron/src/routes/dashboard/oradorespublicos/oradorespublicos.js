let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) {
    throw new Error(err.message);
  }
});

async function load() {
  return new Promise((resolve, reject) => {
    sql = `select * from oradorespublicos`;
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
    const sql = 'SELECT * FROM oradorespublicos WHERE id = ?';
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
    aprobado,
    correoElectronico,
    celular,
    telefono,
    nombramiento
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
  UPDATE oradorespublicos SET
  id = ?,
  nombre = ?,
  apellidos = ?,
  aprobado = ?,
  correoElectronico = ?,
  celular = ?,
  telefono = ?,
  nombramiento = ?
  WHERE id = ?
  `;
  }

  await db.serialize(async () => {
    await db.run('BEGIN TRANSACTION');
    await db.run(sql, [
    id,
    nombre,
    apellidos,
    aprobado,
    correoElectronico,
    celular,
    telefono,
    nombramiento
], (_err) => {
  if (_err) {
    console.log(_err.message);
    db.run('ROLLBACK');
  } else {
    alert(`Orador actualizado`);
    db.run('COMMIT');
  }
});
    }
  )
}

export {load, loadById, save};