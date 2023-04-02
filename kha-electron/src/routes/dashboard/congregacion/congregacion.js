function save(form) {
    let sql;
    const sqlite = require('sqlite3').verbose();
    const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
        if (err) return console.error(err)
    });

    const {
        c_nombre, 
        c_num, 
        c_d_entresemana, 
        c_h_entresemana, 
        d_finsemana, 
        h_finsemana, 
        direccion,
        poblacion,
        s_nombre, 
        s_numero, 
        circuito
     } = form;

     alert(c_nombre);

    db.serialize(() => {
        db.run('BEGIN TRANSACTION');
    
        sql = `update congregacion set nombre = ?, numero = ?, d_entresemana = ?, h_entresemana = ?, d_finsemana = ?, h_finsemana = ?, direccion = ?, poblacion = ?, n_super = ?, t_super = ?, circuito = ? where id = ?`
        db.run(sql, [c_nombre, c_num, c_d_entresemana, c_h_entresemana, d_finsemana, h_finsemana, direccion, poblacion, s_nombre, s_numero, circuito, 1], (_err) => {
          if (_err) {
            console.log(_err.message);
            db.run('ROLLBACK');
          } else {
            alert(`Registro actualizado`);
            db.run('COMMIT');
          }
        })
    })

 }

 export {save};