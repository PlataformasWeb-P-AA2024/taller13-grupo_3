from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/api/"
AUTH = ('uuunin', 'qwerty')  # Reemplaza con tus credenciales

@app.route('/edificios', methods=['GET'])
def listar_edificios():
    response = requests.get(f"{API_URL}edificios/", auth=AUTH)
    return jsonify(response.json())

@app.route('/departamentos', methods=['GET'])
def listar_departamentos():
    response = requests.get(f"{API_URL}departamentos/", auth=AUTH)
    return jsonify(response.json())

@app.route('/edificios', methods=['POST'])
def crear_edificio():
    data = request.json
    response = requests.post(f"{API_URL}edificios/", json=data, auth=AUTH)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)