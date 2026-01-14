import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Crear la app Flask
app = Flask(__name__)
CORS(app)  # Permite que la app Flutter (o cualquier frontend) pueda hacer peticiones

# Obtener la API Key de OpenAI desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/plan", methods=["POST"])
def generate_plan():
    data = request.json
    # Aquí recibimos por ejemplo {"destino": "Paris", "dias": 3}
    destino = data.get("destino", "desconocido")
    dias = data.get("dias", 1)

    # Esto es un ejemplo de respuesta, en producción aquí iría la llamada a OpenAI
    respuesta = f"Plan de viaje para {destino} durante {dias} día(s): actividades recomendadas."

    # Si quisieras llamar a OpenAI, sería algo como:
    # completion = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": f"Plan de viaje para {destino} por {dias} días"}]
    # )
    # respuesta = completion.choices[0].message.content

    return jsonify({"plan": respuesta})

if __name__ == "__main__":
    # IMPORTANTE: host 0.0.0.0 para que Railway pueda acceder
    app.run(host="0.0.0.0", port=8080, debug=False)
