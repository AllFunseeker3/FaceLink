Empleados
IDEmpleados as int as Primarykey,
Nombre as string (30) not null,
ApellidoP as string (30) not null,
ApellidoM as String (30) not null,
FechaNacimiento as date not null

Relacion_EmpleadosDocumentos
--TablaRelacional
IDRelacion as int as primary key,
IDDocumentos as int,
IDEmpleados as int

Tabla Documentos
IDDocumentos as int,
Tipo as string (20),
Ruta as String (100)

Tabla FechaHora
--LOG--
IDHorario as int
IDEmpleados as int
Fecha as date
hora as TIME
