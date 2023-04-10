let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) return console.error(err)
});

function load() {
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

function save(form) {
  const {
    nombre, 
    apellidos
  } = form;

  db.serialize(() => {
    db.run('BEGIN TRANSACTION');

    sql = `insert into publicadores (nombre, apellidos) values (?, ?)`
    db.run(sql, [
      nombre,
      apellidos
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

export {load, save};