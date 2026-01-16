from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

# OpenAI API Key desde Railway (variable de entorno)
openai.api_key = os.getenv("OPENAI_API_KEY")


# ✅ Ruta raíz (OBLIGATORIA para producción)
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Travel AI Backend running"
    })


# ✅ Endpoint real que usará Flutter
@app.route("/plan", methods=["POST"])
def generar_plan():
    data = request.get_json()

    if not data or "prompt" not in data:
        return jsonify({"error": "Falta el campo 'prompt'"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en viajes"},
                {"role": "user", "content": data["prompt"]}
            ]
        )

        plan = response.choices[0].message.content
        return jsonify({"plan": plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
