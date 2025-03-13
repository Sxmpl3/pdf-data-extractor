import mysql.connector
from mysql.connector import Error
import datetime

def save_data_to_db(host, database, user, password, factura):
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Insertar la factura en la tabla 'facturas'
            query_factura = """
            INSERT INTO facturas (numero, fecha, direccion, importe_total)
            VALUES (%s, %s, %s, %s)
            """
            values_factura = (
                factura['Facturas']['numero'],
                factura['Facturas']['fecha'],
                factura['Facturas']['direccion'],
                factura['Facturas']['importe_total']
            )
            cursor.execute(query_factura, values_factura)

            # Obtener el ID de la factura recién insertada
            factura_id = cursor.lastrowid

            # Insertar los productos en la tabla 'productos'
            query_producto = """
            INSERT INTO productos (factura_id, nombre, cantidad, precio)
            VALUES (%s, %s, %s, %s)
            """
            for producto in factura['Facturas']['producto']:
                values_producto = (
                    factura_id,
                    producto['nombre'],
                    producto['cantidad'],
                    producto['precio']
                )
                cursor.execute(query_producto, values_producto) # Insertamos cada producto en la base de datos

            connection.commit() # Hacemos commit para confirmar los cambios

            cursor.close()
            connection.close()

            return True # Retornamos True si se guardaron los datos correctamente
    except:
        return False #  Retornamos False si no se ha podido conectar a la base de datos, etc...

