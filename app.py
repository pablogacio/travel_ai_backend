from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def health():
    return "OK", 200

@app.route("/plan", methods=["POST"])
def generar_plan():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "No se proporcionó 'prompt'"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente de viajes"},
                {"role": "user", "content": data["prompt"]}
            ]
        )

        plan = response.choices[0].message.content
        return jsonify({"plan": plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 👇 SOLO para local, NO Railway
if __name__ == "__main__":
    app.run(debug=True)
