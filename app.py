from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite peticiones desde cualquier origen (Flutter web/app)

@app.route("/generar", methods=["POST"])
def generar_itinerario():
    data = request.get_json()

    destino = data.get("destino", "No definido")
    dias = data.get("dias", 1)
    presupuesto = data.get("presupuesto", 0)
    tipo_viaje = data.get("tipoViaje", "Normal")
    coche = data.get("cocheAlquiler", "No")
    evitar = data.get("evitar", "")

    # Generamos un itinerario simple (por ahora)
    itinerario = f"Itinerario para {destino} ({tipo_viaje}):\n"
    for i in range(1, dias + 1):
        itinerario += f"  Día {i}: Actividades recomendadas.\n"

    if coche.lower() == "sí":
        itinerario += "\nRecuerda que tienes coche de alquiler para moverte libremente.\n"
    if evitar:
        itinerario += f"\nEvitar: {evitar}\n"

    return jsonify({"itinerario": itinerario})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
