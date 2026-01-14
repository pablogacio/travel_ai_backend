from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend activo"})

@app.route("/plan", methods=["POST"])
def plan_trip():
    data = request.get_json()
    # aquí iría tu lógica de OpenAI o backend
    return jsonify({"plan": "Ejemplo de plan de viaje"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
