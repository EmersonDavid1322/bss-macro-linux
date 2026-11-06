import time
from threading import Thread
#Funciones
from src.carga_json import cargar_json
from src.errores.errores import ErrorMacro
from src.patrones_movimiento.ejecutar_ruta import realizar_ruta
from src.rutas import ruta_json_sunflower_fields
from src.patrones_movimiento.moviento_en_campos import bucle_farmeo

def contador():
    print("El programa de ejecutara en 5 segundos, coloque la pantalla de Bee Swarm Simulator como principal")
    for i in range(1,6):
        print("Segundo: ", i)
        time.sleep(1)

def ejecutar_macro():
    ruta = cargar_json.leer_json(ruta_json_sunflower_fields())
    contador()

    realizar_ruta(ruta)

    #Hilo movimiento
    hilo_movimiento = Thread(target=bucle_farmeo(ruta))
    hilo_movimiento.start()
    hilo_movimiento.join()
    print("Hilo Bucle Movimiento lanzado")

def main():
    try:
       ejecutar_macro()
    except ErrorMacro as e:
        print("Ocurrió un error inesperado: ", str(e))
    except KeyboardInterrupt:
        print("El programa termino por una señal de tipo 'SIGINT'")

if __name__ == '__main__':
    main()