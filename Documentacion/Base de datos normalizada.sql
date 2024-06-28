drop database FaceLink;  
CREATE DATABASE FaceLink;  
USE FaceLink;  

-- Creación de la tabla Horarios
CREATE TABLE Horarios (
    IDHorario INT PRIMARY KEY,
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
INSERT INTO Horarios (IDHorario,HoraEntrada, HoraSalida) VALUES (1,'08:00:00', '14:00:00');  
INSERT INTO Horarios (IDHorario,HoraEntrada, HoraSalida) VALUES (2,'14:00:00', '21:00:00');  
INSERT INTO Horarios (IDHorario,HoraEntrada, HoraSalida) VALUES (3,'08:00:00', '21:00:00');  

-- Inserción de registros en la tabla Empleados
INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, FechaNacimiento, IDHorario,FotoRuta)
VALUES ('Cesar', 'Ceron', 'Velazquez', '2001-05-23', 2,'C:/rostros/1'),
('Ricardo', 'Velasquez', 'Galicia', '2014-04-12', 3,'C:/rostros/1');  

-- Inserción de registros en la tabla Documentos
INSERT INTO Documentos (Tipo, Ruta) VALUES ('Curriculum', '/documentos/empleados/1/cv.pdf');  
INSERT INTO Documentos (Tipo, Ruta) VALUES ('Acta de defuncion', '/documentos/empleados/2/cv.pdf');  

-- Inserción de registros en la tabla Relacion_EmpleadosDocumentos
INSERT INTO Relacion_EmpleadosDocumentos (IDRelacion,IDDocumentos, IDEmpleados)
VALUES (1,1, 1),
(2, 2, 2);  

-- Inserción de registros en la tabla LOGFechaHora
-- Registro de una entrada
INSERT INTO LOGFechaHora (IDEmpleados, Fecha, Hora, Entrada)
VALUES (1, '2024-06-08', '08:00:00', TRUE),
(1, '2024-06-08', '21:00:00', FALSE),
(2, '2024-06-08', '08:00:00', TRUE),
(2, '2024-06-08', '12:00:00', FALSE)
;  

--Procedimientos Almacenados
--InicializarRegistros
DELIMITER $$

CREATE PROCEDURE InicializarRegistros()
BEGIN
    SELECT 
        e.IDEmpleados AS id, 
        e.Nombre AS nombre, 
        e.ApellidoP AS apellido_paterno, 
        e.ApellidoM AS apellido_materno, 
        l1.Fecha AS fecha, 
        l1.Hora AS hora_ingreso, 
        l2.Hora AS hora_salida
    FROM 
        Empleados e
    JOIN 
        LOGFechaHora l1 ON e.IDEmpleados = l1.IDEmpleados AND l1.Entrada = TRUE
    LEFT JOIN 
        LOGFechaHora l2 ON e.IDEmpleados = l2.IDEmpleados AND l1.Fecha = l2.Fecha AND l2.Entrada = FALSE AND l2.Hora > l1.Hora
    WHERE 
        l2.IDLog IS NULL OR l2.IDLog = (
            SELECT MIN(l3.IDLog)
            FROM LOGFechaHora l3
            WHERE l3.IDEmpleados = e.IDEmpleados AND l3.Fecha = l1.Fecha AND l3.Entrada = FALSE AND l3.Hora > l1.Hora
        )
    ORDER BY 
        e.IDEmpleados, l1.Fecha;  
END$$

DELIMITER ;  
--Fin Proceso inicializador registros.

---proceso lista empleados
DELIMITER //

DELIMITER //

CREATE PROCEDURE ConsultarEmpleadosConHorarios()
BEGIN
    SELECT 
        E.IDEmpleados,
        E.Nombre,
        E.ApellidoP,
        E.ApellidoM,
        E.FechaNacimiento,
        H.HoraEntrada,
        H.HoraSalida
    FROM 
        Empleados E
    JOIN 
        Horarios H ON E.IDHorario = H.IDHorario;
END //

DELIMITER ;




----






--Proceso almacenado para Inicializar EMpleados
DELIMITER //

CREATE PROCEDURE InicializarEmpleados(
    IN p_IDEmpleado INT
)
BEGIN
    SELECT lf.IDLog AS 'id',
           e.Nombre,
           e.ApellidoP,
           e.ApellidoM,
           e.FechaNacimiento AS 'Fecha',
           lf.Hora AS 'ingreso',
           h.HoraSalida AS 'salida'
    FROM LOGFechaHora lf
    INNER JOIN Empleados e ON lf.IDEmpleados = e.IDEmpleados
    INNER JOIN Horarios h ON e.IDHorario = h.IDHorario
    WHERE lf.IDEmpleados = p_IDEmpleado;  
END //

DELIMITER ;  



DELIMITER //

CREATE PROCEDURE InsertarEmpleadoConDocumento(
    IN p_Nombre VARCHAR(30),
    IN p_ApellidoP VARCHAR(30),
    IN p_ApellidoM VARCHAR(30),
    IN p_FechaNacimiento DATE,
    IN p_IDHorario INT,
    IN p_FotoRuta VARCHAR(255),
    IN p_TipoDocumento VARCHAR(20),
    IN p_RutaDocumento VARCHAR(255)
)
BEGIN
    DECLARE lastIDEmpleados INT;
    DECLARE lastIDDocumentos INT;
    
    -- Insertar el empleado
    INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, FechaNacimiento, IDHorario, FotoRuta)
    VALUES (p_Nombre, p_ApellidoP, p_ApellidoM, p_FechaNacimiento, p_IDHorario, p_FotoRuta);
    
    -- Obtener el último ID insertado en la tabla Empleados
    SET lastIDEmpleados = LAST_INSERT_ID();
    
    -- Insertar el documento
    INSERT INTO Documentos (Tipo, Ruta)
    VALUES (p_TipoDocumento, p_RutaDocumento);
    
    -- Obtener el último ID insertado en la tabla Documentos
    SET lastIDDocumentos = LAST_INSERT_ID();
    
    -- Crear la relación entre el empleado y el documento
    INSERT INTO Relacion_EmpleadosDocumentos (IDDocumentos, IDEmpleados)
    VALUES (lastIDDocumentos, lastIDEmpleados);
END //

DELIMITER ;


--FIn PRoceos