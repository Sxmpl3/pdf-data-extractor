import openai # Libreria usada para
import json # Libreria utilizada para convertir la respuesta de GPT 4 a un diccionario JSON


openai.api_key = 'api'

def extract_data_from_text(text):
    prompt = f"Extrae del siguiente texto la información en formato JSON, el formato debe de ser así, recuerda no comentar nada, solamente responde con el JSON:\n{{\n  \"Facturas\": {{\n    \"numero\": \"937492\",\n    \"fecha\": \"08/02/2025\",\n    \"direccion\": \"Plaza Alta, Algeciras\",\n    \"producto\": [\n      {{\n        \"nombre\": \"Ordenador Portatil HP\",\n        \"cantidad\": 3,\n        \"precio\": \"329.99 €\"\n      }}\n    ],\n    \"importe_total\": \"989.97\"\n  }}\n}} El texto es: {text}" # Creamos el prompt para la IA
    
    # Creamos el mensaje que enviaremos a la IA con las siguientes instrucciones
    messages = [
        {"role": "system", "content": "Eres un útil asistente que crea JSON dependiendo del contenido del mismo y de lo que se te pida, solamente envias el JSON!!!!"},
        {"role": "user", "content": f"{prompt}"}
    ]

    # Realizamos la llamada a la API de OpenAI para obtener la respuesta del texto en formato JSON
    try:
            response = openai.ChatCompletion.create(
                model="gpt-4", # El modelo de IA que usaremos
                messages=messages,
                max_tokens=1024 # El numero maximo de tokens que la IA puede generar en respuesta
            )
    except openai.OpenAIError as e:
        return False

    result = response.choices[0].message['content'].strip() # Obtenemos el texto de la respuesta
    factura = json.loads(result) # Convertimos la respuesta a un diccionario JSON

    return factura


