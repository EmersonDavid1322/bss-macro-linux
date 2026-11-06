import sys
#Funciones
from src.errores.errores import ErrorTecla
from src.patrones_movimiento.movimiento import MAPEO_TECLAS, movimiento_punto_a_b
from src.patrones_movimiento.validar import validar_teclas

def realizar_ruta(ruta_movimiento):
    try:
        print("Comprobando ruta...")
        validar_teclas(teclas_permitidas=MAPEO_TECLAS, teclas_ingresadas=ruta_movimiento["patron_camino"],
                       campo_ruta=ruta_movimiento["destino"])
        print("Ruta Validada")
        movimiento_punto_a_b(ruta_movimiento)
    except ErrorTecla as error:
        print(str(error))
        print("Error de tecla detectado deteniendo el programa")
        sys.exit(1)