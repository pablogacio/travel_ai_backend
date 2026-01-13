from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen (tu app Flutter)

@app.route('/')
def home():
    return "API de Travel AI funcionando!"

@app.route('/generar_itinerario', methods=['POST'])
def generar_itinerario():
    data = request.get_json()

    # Recogemos los campos del formulario
    destino = data.get('destino', 'desconocido')
    dias = data.get('dias', 1)
    presupuesto = data.get('presupuesto', 0)
    tipo_viaje = data.get('tipo_viaje', 'normal')
    coche_alquiler = data.get('coche_alquiler', 'no')
    no_visitar = data.get('no_visitar', '')

    # Creamos un itinerario de ejemplo (provisional)
    itinerario = []
    for i in range(1, int(dias)+1):
        actividades = [f"Actividades recomendadas para {destino} en el día {i}"]
        itinerario.append({
            "dia": f"Día {i}",
            "actividades": actividades
        })

    # Retornamos en JSON
    return jsonify({
        "destino": destino,
        "dias": dias,
        "presupuesto": presupuesto,
        "tipo_viaje": tipo_viaje,
        "coche_alquiler": coche_alquiler,
        "no_visitar": no_visitar,
        "itinerario": itinerario
    })

if __name__ == '__main__':
    app.run(debug=True)
