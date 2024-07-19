from flask import Flask, jsonify, request, render_template
import requests
import json

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/api/"
AUTH = ('uuunin', 'qwerty')  # Reemplaza con tus credenciales


@app.route('/obteneredificios')
def listar_edificios():
    response = requests.get(f"{API_URL}edificios/")
    return render_template('edificios.html', edificios=response.json(), numero_edificios=len(response.json()))


@app.route('/departamentos', methods=['GET'])
def listar_departamentos():
    r = requests.get("http://127.0.0.1:8000/api/departamentos/", auth=AUTH)

    datos = r.json()
    datos2 = []
    for d in datos:
        datos2.append({
            'nombre_propietario': d['nombre_propietario'],
            'costo': d['costo'],
            'numero_cuartos': d['numero_cuartos'],
            'edificio': obtener_edificio(f"{API_URL}edificios/{d['edificio']}/")
        })
    return render_template("departamentos.html", datos=datos2, numero=len(datos))


def obtener_edificio(url):
    response = requests.get(url, auth=AUTH)
    nombre = response.json()['nombre']
    return nombre


@app.route('/nuevo_edificio', methods=['GET', 'POST'])
def nuevo_edificio():
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'direccion': request.form['direccion'],
            'ciudad': request.form['ciudad'],
            'tipo': request.form['tipo']
        }
        response = requests.post(f"{API_URL}edificios/", json=data, auth=AUTH)
        if response.status_code == 201:
            return render_template('edificio_creado.html', edificio=response.json())
        else:
            return render_template('nuevo_edificio.html', error="Error al crear el edificio. Intente nuevamente.")
    return render_template('nuevo_edificio.html')


if __name__ == '__main__':
    app.run()
