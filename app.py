from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

# API Key de OpenAI desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/plan", methods=["POST"])
def generar_plan():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "No se proporcionó 'prompt'"}), 400

    prompt = data["prompt"]

    try:
        # Generamos el plan usando OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente de viajes"},
                {"role": "user", "content": prompt}
            ]
        )
        plan = response.choices[0].message.content
        return jsonify({"plan": plan})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Railway asigna el puerto a través de la variable PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
