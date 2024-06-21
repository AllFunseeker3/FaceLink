CREATE DATABASE FaceLink;
USE FaceLink;

-- Creación de la tabla Horarios
CREATE TABLE Horarios (
    IDHorario INT PRIMARY KEY AUTO_INCREMENT,
    HoraEntrada TIME NOT NULL,
    HoraSalida TIME NOT NULL
);

-- Creación de la tabla Empleados
CREATE TABLE Empleados (
    IDEmpleados INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL,
    ApellidoP VARCHAR(30) NOT NULL,
    ApellidoM VARCHAR(30) NOT NULL,
    FechaNacimiento DATE NOT NULL,
    IDHorario INT,
	FotoRuta VARCHAR(255),
    FOREIGN KEY (IDHorario) REFERENCES Horarios(IDHorario)
);

-- Creación de la tabla Documentos
CREATE TABLE Documentos (
    IDDocumentos INT PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(20) NOT NULL,
    Ruta VARCHAR(255) NOT NULL
);

-- Creación de la tabla Relacion_EmpleadosDocumentos
CREATE TABLE Relacion_EmpleadosDocumentos (
    IDRelacion INT PRIMARY KEY AUTO_INCREMENT,
    IDDocumentos INT,
    IDEmpleados INT,

    FOREIGN KEY (IDDocumentos) REFERENCES Documentos(IDDocumentos),
    FOREIGN KEY (IDEmpleados) REFERENCES Empleados(IDEmpleados)
);

-- Creación de la tabla LOGFechaHora
CREATE TABLE LOGFechaHora (
    IDLog INT PRIMARY KEY AUTO_INCREMENT,
    IDEmpleados INT NOT NULL,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
	Entrada BOOLEAN NOT NULL,
    FOREIGN KEY (IDEmpleados) REFERENCES Empleados(IDEmpleados)
);

------------------------------Primera entrada solo para Debug_________________-
-- Inserción de registros en la tabla Horarios
INSERT INTO Horarios (HoraEntrada, HoraSalida) VALUES ('08:00:00', '17:00:00');

-- Inserción de registros en la tabla Empleados
INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, FechaNacimiento, IDHorario,FotoRuta)
VALUES ('Juan', 'Pérez', 'Gómez', '1985-06-15', 1,'C:/rutaALV');

-- Inserción de registros en la tabla Documentos
INSERT INTO Documentos (Tipo, Ruta) VALUES ('Curriculum', '/documentos/empleados/1/cv.pdf');

-- Inserción de registros en la tabla Relacion_EmpleadosDocumentos
INSERT INTO Relacion_EmpleadosDocumentos (IDDocumentos, IDEmpleados)
VALUES (1, 1);

-- Inserción de registros en la tabla LOGFechaHora
-- Registro de una entrada
INSERT INTO LOGFechaHora (IDEmpleados, Fecha, Hora, Entrada)
VALUES (1, '2024-06-08', '08:00:00', TRUE);

-- Registro de una salida
INSERT INTO LOGFechaHora (IDEmpleados, Fecha, Hora, Entrada)
VALUES (1, '2024-06-08', '17:00:00', FALSE);
