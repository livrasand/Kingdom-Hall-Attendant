
DROP INDEX congregacion_id_idx;

DROP TABLE congregacion;

CREATE TABLE congregacion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre NVARCHAR,
    numero NVARCHAR,
    d_entresemana NVARCHAR,
    h_entresemana NVARCHAR,
    d_finsemana NVARCHAR,
    h_finsemana NVARCHAR,
    direccion NVARCHAR,
    poblacion NVARCHAR,
    s_nombre NVARCHAR,
    s_numero NVARCHAR,
    circuito NVARCHAR,
);

CREATE UNIQUE INDEX IF NOT EXISTS congregacion_id_idx ON congregacion (
    id 
);