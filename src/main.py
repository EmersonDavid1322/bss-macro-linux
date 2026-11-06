import time
#Funciones
from src.carga_json import cargar_json
from src.errores.errores import ErrorMacro
from src.patrones_movimiento.ejecutar_ruta import realizar_ruta
from src.rutas import ruta_json_sunflower_fields

def contador():
    print("El programa de ejecutara en 5 segundos, coloque la pantalla de Bee Swarm Simulator como principal")
    for i in range(1,6):
        print("Segundo: ", i)
        time.sleep(1)

def main():
    try:
       ruta = cargar_json.leer_json(ruta_json_sunflower_fields())
       contador()
       realizar_ruta(ruta)
    except ErrorMacro as e:
        print("Ocurrió un error inesperado: ", str(e))

if __name__ == '__main__':
    main()