let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) {
    throw new Error(err.message);
  }
  console.log('Connected to the database.');
});

async function load() {
  console.log('Fetching data from the database...');
  return new Promise((resolve, reject) => {
    sql = `SELECT * FROM oradorespublicos`;
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

function loadById(id) {
  console.log(`Fetching data for ID ${id} from the database...`);
  return new Promise((resolve, reject) => {
    const sql = 'SELECT * FROM oradorespublicos WHERE id = ?';
    db.get(sql, [id], (err, row) => {
      if (err) {
        console.error('Error fetching data:', err.message);
        reject(err);
      } else {
        console.log('Data fetched:', row);
        resolve(row);
      }
    });
  });
}

async function save(form) {
  console.log('Saving data to the database:', form);
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
    const updateSql = `
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

    await db.serialize(async () => {
      await db.run('BEGIN TRANSACTION');
      await db.run(updateSql, [
        id,
        nombre,
        apellidos,
        aprobado,
        correoElectronico,
        celular,
        telefono,
        nombramiento,
        id  // Add id here for the WHERE clause
      ], (_err) => {
        if (_err) {
          console.error('Error saving data:', _err.message);
          db.run('ROLLBACK');
        } else {
          console.log('Data saved/updated successfully.');
          db.run('COMMIT');
        }
      });
    });
  }
}

export { load, loadById, save };