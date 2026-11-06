import json

def leer_json(ruta):
    with open(ruta, 'r') as f:
        return json.load(f)