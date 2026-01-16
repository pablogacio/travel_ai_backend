from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

# OpenAI API Key desde Railway Variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/plan", methods=["POST"])
def generar_plan():
    # Forzamos lectura de JSON (clave para evitar el 400)
    data = request.get_json(force=True, silent=True)

    if not data or "prompt" not in data:
        return jsonify({"error": "Falta el campo 'prompt'"}), 400

    prompt = data["prompt"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en viajes"},
                {"role": "user", "content": prompt}
            ]
        )

        plan = response.choices[0].message.content
        return jsonify({"plan": plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ⚠️ IMPORTANTE: NO levantar Flask aquí en Railway
# Gunicorn se encarga
