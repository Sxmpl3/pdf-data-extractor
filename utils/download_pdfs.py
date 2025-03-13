import imaplib
import email
from email.header import decode_header
import os

# Conexion y logueo de la cuenta
def connect_to_mail(email_account, email_password):
    mail = imaplib.IMAP4_SSL("imap.ionos.es") # Seleccionamos el protocolo SSL de IMAP y el servidor que vamos a usar
    mail.login(email_account, email_password) # Login al email
    return mail # Retornamos la conexion para poder usarla para descargar los pdfs

# Descarga de los PDFs del correo
def download_pdfs(mail, save_folder):
    if not os.path.exists(save_folder): # Asegurarse de que el directorio existe, si no existe, se crea
        os.makedirs(save_folder)

    mail.select("inbox")  # Seleccionamos la bandeja de entrada

    status, mensajes = mail.search(None, 'ALL')  # Podemos filtrar por "UNSEEN" si solo queremos usar los no leidos, en este caso usamos ALL ya que si no tendria que reenviar la factura para que pruebes el script
    mensajes = mensajes[0].split() # Convertimos los IDs de los mensajes a una lista

    for num in mensajes: # Recorremos cada mensaje
        status, data = mail.fetch(num, "(RFC822)") # Obtenemos el mensaje y sus partes
        for response_part in data: # Recorremos cada parte del mensaje
            if isinstance(response_part, tuple): # Si la respuesta es un mensaje
                msg = email.message_from_bytes(response_part[1]) # Obtenemos el titulo del mensaje
                subject, encoding = decode_header(msg["Subject"])[0] # Obtener el asunto del correo y el encoding utilizado
                if isinstance(subject, bytes): # Si el asunto es bytes, lo convertimos a string (texto)
                    subject = subject.decode(encoding or "utf-8")

                for part in msg.walk(): # Recorremos cada parte del mensaje
                    if part.get_content_maintype() == "multipart": # Ignoramos las partes que no son PDFs
                        continue
                    if part.get_content_type() == "application/pdf": # En casso de que tenga un PDF adjunto
                        filename = part.get_filename() # "Guardaremos" el archivo en una variable
                        if filename: # Si existe el archivo
                            filepath = os.path.join(save_folder, filename) # Creamos el path del archivo
                            with open(filepath, "wb") as f: # Escribimos el contenido del PDF en el archivo
                                f.write(part.get_payload(decode=True)) # Descargamos el PDF

    mail.logout()
