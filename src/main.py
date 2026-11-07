#!/usr/bin/env python3
import time
from threading import Thread
import argparse
#Funciones
from src.carga_json import cargar_json
from src.errores.errores import ErrorMacro
from src.patrones_movimiento.ejecutar_ruta import realizar_ruta
from src.rutas import ruta_json_campo
from src.patrones_movimiento.moviento_en_campos import bucle_farmeo
from src.estado_macro import cambiar_estado
from  src.patrones_movimiento.control_mause import activar_clicks

def contador():
    print("El programa de ejecutara en 5 segundos, coloque la pantalla de Bee Swarm Simulator como principal")
    for i in range(1,6):
        print("Segundo: ", i)
        time.sleep(1)

def ejecutar_macro(argumentos):
    ruta = cargar_json.leer_json(ruta_json_campo(argumentos.campo))
    contador()

    realizar_ruta(ruta)
    #Hilos
    hilo_movimiento = Thread(target=bucle_farmeo, args=(ruta,), daemon=True)
    hilo_clicks = Thread(target=activar_clicks, daemon=True)

    hilo_movimiento.start()
    print("Hilo Bucle Movimiento lanzado")

    hilo_clicks.start()
    print("Hilo Bucle Clicks lanzado")

    hilo_movimiento.join()
    hilo_clicks.join()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('campo', type=str, help='Nombre del campo')
    args = parser.parse_args()
    try:
       ejecutar_macro(argumentos=args)
    except FileNotFoundError:
        print(f"EL argumento '{args.campo}' no es un campo existente, por favor ingréselo en ingles y minúsculas")
    except ErrorMacro as e:
        print("Ocurrió un error inesperado: ", str(e))
    except KeyboardInterrupt:
        print("El programa termino por una señal de tipo 'SIGINT'")
    finally:
        cambiar_estado()

if __name__ == '__main__':
    main()