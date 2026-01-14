from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta de prueba para verificar que el backend funciona
@app.route("/")
def home():
    return jsonify({"message": "Backend activo"})

# Ruta real de la API para tu plan de viaje
@app.route("/plan", methods=["POST"])
def plan_trip():
    data = request.get_json()
    destino = data.get("destino", "Mundo")
    # Aquí iría tu lógica de OpenAI o cualquier procesamiento
    plan = {
        "dia_1": f"Actividades recomendadas en {destino} para el día 1",
        "dia_2": f"Actividades recomendadas en {destino} para el día 2",
        "dia_3": f"Actividades recomendadas en {destino} para el día 3"
    }
    return jsonify(plan)

if __name__ == "__main__":
    # Muy importante: host 0.0.0.0 y puerto 8080 para Railway
    app.run(host="0.0.0.0", port=8080)
