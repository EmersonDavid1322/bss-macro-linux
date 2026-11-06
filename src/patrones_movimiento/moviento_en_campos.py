import time
import  threading
from evdev import UInput, ecodes as e
#scripts
from src.patrones_movimiento.validar import identificar_tecla
from src.estado_macro import activo

MAPEO_TECLAS = {
    "W": e.KEY_W,
    "A": e.KEY_A,
    "S": e.KEY_S,
    "D": e.KEY_D
}

teclas_permitidas = {
    e.EV_KEY: list(MAPEO_TECLAS.values())
}

evento = threading.Event()

def bucle_farmeo(ruta_movimiento):
    print("Iniciando bucle de movimiento")
    with UInput(teclas_permitidas, name='bucle-farmeo') as ui:
        time.sleep(1)
        try:
            while activo:
                for tecla in ruta_movimiento["bucle_farm"]:
                    if not activo:
                        return
                    tecla_codigo = identificar_tecla(tecla["tecla"], MAPEO_TECLAS)

                    if tecla_codigo is not None:

                        ui.write(e.EV_KEY, tecla_codigo, 1)
                        ui.syn()

                        # Tiempo presionado
                        evento.wait(tecla["duracion"])

                        ui.write(e.EV_KEY, tecla_codigo, 0)
                        ui.syn()
                evento.wait(0.05)
        finally:
            print("Finalizando bucle a", ruta_movimiento["destino"])
            for tecla in teclas_permitidas[e.EV_KEY]:
                ui.write(e.EV_KEY, tecla, 0)
            ui.syn()
            print("Finalizado")