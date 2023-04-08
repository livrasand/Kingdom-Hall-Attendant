let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) return console.error(err)
});

function load() {
  return new Promise((resolve, reject) => {
    sql = `select * from congregacion where id=1`;
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
    c_nombre, 
    c_numero, 
    c_d_entresemana, 
    c_h_entresemana, 
    c_d_finsemana, 
    c_h_finsemana, 
    c_direccion,
    c_poblacion,
    c_s_nombre, 
    c_s_numero, 
    c_circuito
  } = form;

  db.serialize(() => {
    db.run('BEGIN TRANSACTION');

    sql = `update congregacion set nombre = ?, numero = ?, d_entresemana = ?, h_entresemana = ?, d_finsemana = ?, h_finsemana = ?, direccion = ?, poblacion = ?, n_super = ?, t_super = ?, circuito = ? where id = ?`
    db.run(sql, [
      c_nombre,
      c_numero,
      c_d_entresemana,
      c_h_entresemana,
      c_d_finsemana,
      c_h_finsemana,
      c_direccion,
      c_poblacion,
      c_s_nombre,
      c_s_numero,
      c_circuito, 
      1
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