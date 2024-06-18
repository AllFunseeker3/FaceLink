import mysql.connector
from mysql.connector import Error

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
            return resultados

    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("La conexión MySQL se ha cerrado")

# Ejemplo de uso:
resultados = ejecutar_consulta("SELECT * FROM Empleados")
if resultados:
    for fila in resultados:
        print(fila)
