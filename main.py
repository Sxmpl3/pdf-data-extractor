import os

from utils.download_pdfs import connect_to_mail, download_pdfs # Conexion al correo y descarga de PDFs
from utils.extract_content_pdf import extract_pdf_content # Extracción de texto del PDF
from utils.extract_data import extract_data_from_text # Obtencion de un JSON con los datos de la factura gracias a la IA
from utils.save_data_to_db import save_data_to_db # Guardar los datos de la factura en la base de datos

email_account = ""
email_password = ""


# Carpeta donde guardaremos las facturas
save_folder = "Facturas"

# Credenciales base de datos local
host = "localhost"
database = "finanzas"
user = "root"
password = ""

# Funcion principal
def main():
    try:
        mail = connect_to_mail(email_account, email_password) # Realizamos conexion al correo
        if mail:
            print("Conexion al correo realizada con éxito")
        else:
            print("Error de conexion")
            return
        
        download_pdfs(mail, save_folder)
        text = extract_pdf_content("Facturas/*.pdf")
        if text:
            print("Texto extraido con éxito")
        else:
            print("Error al extraer el texto")
            return

        factura = extract_data_from_text(text)

        if factura:
            print("Factura extraida con éxito")
        else:
            print("Error al extraer la factura")
            return
        
        if save_data_to_db(host, database, user, password, factura):
            print("Factura guardada con éxito")
        else:
            os.system("cls")
            print(f"Factura:\n{factura}")
        
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()

