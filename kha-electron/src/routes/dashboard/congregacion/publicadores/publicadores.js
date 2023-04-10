let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) return console.error(err)
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
    apellidos
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
    // Si el registro ya existe, actualizarlo
    sql = `UPDATE publicadores SET nombre = ?, apellidos = ? WHERE id = ?`;
  } else {
    // Si el registro no existe, insertarlo
    sql = `INSERT OR REPLACE INTO publicadores (nombre, apellidos, id) values (?, ?, ?)`;
  }

  await db.serialize(async () => {
    await db.run('BEGIN TRANSACTION');
    await db.run(sql, [
      nombre,
      apellidos,
      id
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