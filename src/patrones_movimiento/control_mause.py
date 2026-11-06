import  threading
from evdev import UInput, ecodes as e
#scripts
from src.estado_macro import activo

eventos = threading.Event()

permitidas = {
    e.EV_KEY: [e.BTN_LEFT]
}

def activar_clicks():
    with UInput(permitidas) as ui:
        try:
            while activo:
                ui.write(e.EV_KEY, e.BTN_LEFT, 1)
                ui.syn()

                eventos.wait(0.05)

                ui.write(e.EV_KEY, e.BTN_LEFT, 0)
                ui.syn()

                eventos.wait(0.1)
        finally:
            ui.write(e.EV_KEY, e.BTN_LEFT, 0)
            ui.syn()