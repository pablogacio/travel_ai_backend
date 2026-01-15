from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Cliente OpenAI usando variable de entorno (PRODUCCIÓN)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Backend funcionando"}), 200

@app.route("/plan", methods=["POST"])
def generar_plan():
    data = request.get_json(silent=True)

    if not data or "prompt" not in data:
        return jsonify({"error": "Falta el campo 'prompt'"}), 400

    prompt = data["prompt"]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en viajes."},
                {"role": "user", "content": prompt}
            ]
        )

        plan = response.choices[0].message.content
        return jsonify({"plan": plan}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
