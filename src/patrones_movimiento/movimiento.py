import time
from evdev import UInput, ecodes as e
#scripts
from src.patrones_movimiento.validar import validar_teclas, identificar_tecla

MAPEO_TECLAS = {
    "W": e.KEY_W,
    "A": e.KEY_A,
    "S": e.KEY_S,
    "D": e.KEY_D,
    "espacio": e.KEY_SPACE
}

teclas_permitidas = {
    e.EV_KEY: list(MAPEO_TECLAS.values())
}


def movimiento_punto_a_b(ruta_movimiento):
    # Verificar teclas
    validar_teclas(teclas_permitidas=MAPEO_TECLAS, teclas_ingresadas=ruta_movimiento["patron_camino"], campo_ruta=ruta_movimiento["destino"])
    with UInput(teclas_permitidas, name='controlador-punto-a-b') as ui:
        # Espera reconocimiento del sistema
        time.sleep(1)
        try:
            for tecla in ruta_movimiento["patron_camino"]:
                tecla_codigo = identificar_tecla(tecla["tecla"], MAPEO_TECLAS)

                if tecla_codigo is not None:
                    print("Presionando:", tecla["tecla"])

                    ui.write(e.EV_KEY, tecla_codigo, 1)
                    ui.syn()

                    # Tiempo presionado
                    time.sleep(tecla["duracion"])

                    print("Soltando:", tecla["tecla"])
                    ui.write(e.EV_KEY, tecla_codigo, 0)
                    ui.syn()

                time.sleep(0.05)
        finally:
            print("Finalizando ruta a", ruta_movimiento["destino"])
            for tecla in teclas_permitidas[e.EV_KEY]:
                ui.write(e.EV_KEY, tecla, 0)
            ui.syn()
            print("Finalizando")