import os

def ruta_json_campo(nombre_campo):
    return  os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/" + "routes" + "/" + nombre_campo + ".json"