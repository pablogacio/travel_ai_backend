from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)  # Esto permite que tu app Flutter pueda llamar al backend sin CORS errors

# API Key de OpenAI desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/plan", methods=["POST"])
def generar_plan():
    # Obtener JSON del POST
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "Falta el prompt"}), 400

    prompt = data["prompt"]

    # Generar respuesta (ejemplo, reemplaza con tu lógica)
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=300
        )
        plan_text = response.choices[0].text.strip()
        return jsonify({"plan": plan_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Para pruebas locales solo, en Railway el servidor se levanta automáticamente
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)

