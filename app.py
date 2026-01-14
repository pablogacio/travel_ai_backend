from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend de Travel AI funcionando correctamente!"
    })

@app.route("/generar-itinerario", methods=["POST"])
def generar_itinerario():
    data = request.json
    destino = data.get("destino", "tu destino")
    dias = int(data.get("dias", 1))
    presupuesto = float(data.get("presupuesto", 0))
    tipo_viaje = data.get("tipo_viaje", "Turismo")
    coche_alquiler = data.get("coche_alquiler", "No")
    exclusions = data.get("exclusiones", "")

    itinerario = []
    for i in range(1, dias+1):
        itinerario.append(f"Día {i}: Actividades recomendadas para {destino} ({tipo_viaje})")
    
    response = {
        "destino": destino,
        "dias": dias,
        "presupuesto": presupuesto,
        "tipo_viaje": tipo_viaje,
        "coche_alquiler": coche_alquiler,
        "exclusiones": exclusions,
        "itinerario": itinerario
    }
    return jsonify(response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
