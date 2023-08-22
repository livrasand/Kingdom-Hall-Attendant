DROP INDEX configuracion_id_idx;
DROP TABLE configuracion;

CREATE TABLE configuracion (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombres TEXT,
  apellidos TEXT,
  correo_electronico TEXT,
  ubicacion TEXT,
  privilegio INTEGER,
  avatar BLOB 
);

CREATE UNIQUE INDEX IF NOT EXISTS configuracion_id_idx ON configuracion (id);
