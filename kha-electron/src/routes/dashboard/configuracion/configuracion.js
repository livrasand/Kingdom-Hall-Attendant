let sql;
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) return console.error(err)
});

function load() {
  return new Promise((resolve, reject) => {
    sql = `select * from configuracion where id=1`;
    db.all(sql, [], (err, rows) => {
      if (err) {
        console.error(err.message);
        reject(err);
      } else {
        resolve(rows);
      }
    });
  });
}



function save(form) {
  return new Promise((resolve, reject) => {
    const {
      c_nombres,
      c_apellidos,
      c_correo_electronico,
      user_profile_location,
      user_profile_pronouns_select,
      avatarImageData
    } = form;

    db.serialize(() => {
      db.run('BEGIN TRANSACTION');

      sql = `update configuracion set nombres = ?, apellidos = ?, correo_electronico = ?, ubicacion = ?, privilegio = ?, avatar = ? where id = ?`;
      db.run(
        sql,
        [
          c_nombres,
          c_apellidos,
          c_correo_electronico,
          user_profile_location,
          user_profile_pronouns_select,
          avatarImageData,
          1
        ],
        (_err) => {
          if (_err) {
            console.log(_err.message);
            db.run('ROLLBACK', () => {
              reject(_err);
            });
          } else {
            db.run('COMMIT', () => {
              console.log('Datos guardados exitosamente');
              resolve();
            });
          }
        }
      );
    });
  });
}

export { load, save };