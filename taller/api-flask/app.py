from flask import Flask, jsonify, request, render_template
import requests
import json

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/api/"
AUTH = ('uuunin', 'qwerty')  # Reemplaza con tus credenciales

@app.route('/obteneredificios')
def listar_edificios():
    response = requests.get(f"{API_URL}edificios/")
    return render_template('edificios.html', edificios = response.json(), numero_edificios = len(response.json()))

@app.route('/departamentos', methods=['GET'])
def listar_departamentos():
    r = requests.get(f"{API_URL}departamentos/", auth=AUTH)
    datos = r.json()
    numero = len(r.json())
    datos2 = []
    for d in datos:
        datos2.append(

        {
        'nombre_propietario':d['nombre_propietario'],
        'costo':d['costo'],
        'numero_cuartos':d['numero_cuartos'],
        'edificio': obtener_edificio(f"{API_URL}{d['edificio']}") }
        # http://127.0.0.1:8000/api/estudiantes/4/
        # René
        )
    
    
    return render_template('departamentos.html', datos = datos2, numero = numero)

@app.route('/edificios', methods=['POST'])
def crear_edificio():
    data = request.json
    response = requests.post(f"{API_URL}edificios/", json=data, auth=AUTH)
    return jsonify(response.json())


def obtener_edificio(url):
    response = requests.get(url, auth=AUTH)
    response = response.json()
    nombre_edificio = response['nombre']
    return nombre_edificio

if __name__ == '__main__':
    app.run()