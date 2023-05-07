DROP INDEX configuracion_id_idx;

DROP TABLE configuracion;

CREATE TABLE configuracion (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nombres TEXT,
	apellidos TEXT,
	correo_electronico TEXT
);

CREATE UNIQUE INDEX IF NOT EXISTS configuracion_sid_idx ON configuracion (
    id 
);