DROP INDEX publicadores_id_idx;

DROP TABLE publicadores;

CREATE TABLE publicadores (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nombre TEXT,
	apellidos TEXT,
	email TEXT,
	celular TEXT,
	telefono INTEGER
);

CREATE UNIQUE INDEX IF NOT EXISTS publicadores_id_idx ON publicadores (
    id 
);