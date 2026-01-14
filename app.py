import os
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API key desde variable de entorno
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/plan", methods=["POST"])
def generate_plan():
    data = request.json
    prompt = data.get("prompt", "Escribe un plan de viaje")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return jsonify({"plan": response.choices[0].text.strip()})

# Opcional: ruta de prueba en GET para saber si el servidor funciona
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "El backend está activo"})
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
