import time
#Funciones
from src.carga_json import cargar_json
from src.rutas import ruta_json_sunflower_fields
from src.patrones_movimiento.movimiento import movimiento_punto_a_b

def contador():
    print("El programa de ejecutara en 5 segundos, coloque la pantalla de Bee Swarm Simulator como principal")
    for i in range(1,6):
        print("Segundo: ", i)
        time.sleep(1)

def main():
   ruta = cargar_json.leer_json(ruta_json_sunflower_fields())
   contador()
   movimiento_punto_a_b(ruta)

if __name__ == '__main__':
    main()