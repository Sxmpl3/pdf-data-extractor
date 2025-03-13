import fitz  # PyMuPDF, libreria usada para extraer el contenido del pdf
import glob # Utilizada para trabajar con PDFs

def extract_pdf_content(dir):    
    pdf_files = glob.glob(dir) # Obtenemos cuantos PDFs hay en el directorio

    for pdf in pdf_files: # Array para recorrer cada PDF
        doc = fitz.open(pdf)
        text = ""
        
        for pagina in doc: # Recorremos las paginas del documento
            text += pagina.get_text() # Agregamos el texto
        
        return text # Retornamos el texto del pdf
    
    doc.close()