
import mysql.connector
from mysql.connector import *

def conectar_mysql(host, database, usuario, contraseña):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=usuario,
            password=contraseña
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado al servidor MySQL versión {db_info}")
            return connection

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def ejecutar_consulta(consulta):
    connection = conectar_mysql('localhost', 'FaceLink', 'root', '')
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            resultados = [list(fila) for fila in resultados]
            return resultados

    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("La conexión MySQL se ha cerrado")




            
def ejecutar_procedimiento(procedimiento, args=None):
    conexion = conectar_mysql('localhost', 'FaceLink', 'root', '')
    cursor = conexion.cursor()
    try:
            # Llamar al procedimiento almacenado


            cursor.callproc(procedimiento, args=(args))
            
            # Si el procedimiento almacenado devuelve resultados, puedes obtenerlos así:
            for result in cursor.stored_results():
                #print(result.fetchall())
                resultados = result.fetchall()
                resultados = [list(fila) for fila in resultados]
                return resultados
            # Confirmar los cambios en la base de datos
            conexion.commit()
            print("Procedimiento almacenado ejecutado correctamente.")
            
    except Exception as e:
            print(f"Error al ejecutar el procedimiento almacenado: {str(e)}")
            
    finally:
            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

 ##ejemplo de uso consulta
       # for fila in ejecutar_consulta("select * from empleados"):
        #    datos.append(fila)
#Procedimiento
#for fila in ejecutar_procedimiento("ObtenerDatosEmpleados",()):
#    print(fila)
        #Procedimiento con argunmento
#args = (1,)
#for fila in ejecutar_procedimiento("IniciarEmpleado",(1,)):
#    print(fila)



def ejecutar_modificacion(modificacion):
    connection = conectar_mysql('localhost', 'FaceLink', 'root', '')
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(modificacion)
            connection.commit()  # Para asegurar que los cambios se apliquen

            # Devuelve el número de filas afectadas por la operación
            num_filas_afectadas = cursor.rowcount
            return num_filas_afectadas

    except Error as e:
        print(f"Error al ejecutar la modificación: {e}")
        return 0  # En caso de error, retornar 0 o manejar según necesidad

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("La conexión MySQL se ha cerrado")



# ejecutar_procedimiento("InsertarEmpleadoConDocumento",('Juan', 
#     'Perez', 
#     'Lopez', 
#     '1985-04-15', 
#     1, 
#     '/path/to/photo.jpg', 
#     'Contrato', 
#     '/path/to/document.pdf',))