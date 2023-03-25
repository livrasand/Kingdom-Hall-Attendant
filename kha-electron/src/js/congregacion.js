let sql;

sql = `select * from congregacion where id = ?`
db.get(sql, [1], (_err, row) => {
  if (_err) {
    return console.log(_err.message)
  }
  if (row === undefined) {
    sql = 'insert into congregacion (id) values (?)'
    db.run(sql, [1], (_err) => {
      if (_err) {
        console.log(_err.message);
      } else {
        console.log(`Registros actualizados: ${this.lastID}`);
      }
    })
  } else {
    console.log(row);
    let name = document.querySelector('input[name="c_nombre"]');
    name.value = row.nombre;
    let number = document.querySelector('input[name="c_num"]');
    number.value = row.numero

    let d_entresemana = document.getElementsByName('c_d_entresemana');
    for (var i = 0; i < d_entresemana.length; i++) {
      if (d_entresemana[i].value === row.d_entresemana) {
        d_entresemana[i].checked = true;
        break;
      }
    }

    let h_entresemana = document.querySelector('input[name="c_h_entresemana"]');
    h_entresemana.value = row.h_entresemana

    let d_finsemana = document.getElementsByName('c_d_finsemana');
    for (var i = 0; i < d_finsemana.length; i++) {
      if (d_finsemana[i].value === row.d_finsemana) {
        d_finsemana[i].checked = true;
        break;
      }
    }

    let h_finsemana = document.querySelector('input[name="c_h_finsemana"]')
    h_finsemana.value = row.h_finsemana

    let direccion = document.getElementById('c_direccion')
    direccion.value = row.direccion

    let s_nombre = document.querySelector('input[name="c_s_nombre"]')
    s_nombre.value = row.n_super
    let s_numero = document.querySelector('input[name="c_s_numero"]')
    s_numero.value = row.t_super
    let circuito = document.querySelector('input[name="c_circuito"]')
    circuito.value = row.t_super
  }
});

// Formulario Congregación
const form_congregacion = document.getElementById('form-congregacion')
form_congregacion.addEventListener('submit', (e) => {
  e.preventDefault()
  const datos = new FormData(document.getElementById('form-congregacion'))

  const nombre = datos.get('c_nombre')
  const num = datos.get('c_num')
  const d_entresemana = datos.get('c_d_entresemana')
  const h_entresemana = datos.get('c_h_entresemana')
  const h_finsemana = datos.get('c_h_finsemana')
  const d_finsemana = datos.get('c_d_finsemana')
  const direccion = datos.get('c_direccion')
  const poblacion = datos.get('c_poblacion')
  const s_nombre = datos.get('c_s_nombre')
  const s_numero = datos.get('c_s_numero')
  const circuito = datos.get('c_circuito')

  // iniciar una transacción
  db.serialize(() => {
    db.run('BEGIN TRANSACTION');

    sql = `update congregacion set nombre = ?, numero = ?, d_entresemana = ?, h_entresemana = ?, d_finsemana = ?, h_finsemana = ?, direccion = ?, poblacion = ?, n_super = ?, t_super = ?, circuito = ? where id = ?`
    db.run(sql, [nombre, num, d_entresemana, h_entresemana, d_finsemana, h_finsemana, direccion, poblacion, s_nombre, s_numero, circuito, 1], (_err) => {
      if (_err) {
        console.log(_err.message);
        db.run('ROLLBACK');
      } else {
        alert(`Registro actualizado`);
        db.run('COMMIT');
      }
    })
  })

})


