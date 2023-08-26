DROP INDEX oradorespublicos_id_idx;

DROP TABLE oradorespublicos;

CREATE TABLE oradorespublicos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nombre TEXT,
    apellidos TEXT,
    aprobado TEXT,
    correoElectronico TEXT,
    celular TEXT,
    telefono TEXT,
    nombramiento TEXT	
);

CREATE UNIQUE INDEX IF NOT EXISTS oradorespublicos_id_idx ON oradorespublicos (
    id 
);