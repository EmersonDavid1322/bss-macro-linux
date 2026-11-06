# bss-macro-linux

Macro para **Bee Swarm Simulator** (Roblox) hecho en Python y pensado para **Linux con Wayland**. Simula un teclado virtual a nivel del kernel (`uinput`), sin inyectar código en el juego ni usar exploits.

> Proyecto de aprendizaje, en desarrollo. Úsalo bajo tu propia responsabilidad.

## Cómo funciona

1. Las rutas se describen en archivos **JSON**, separadas del código.
2. Un ejecutor lee cada ruta y la convierte en pulsaciones de teclas.
3. Un teclado virtual (`python-evdev`) envía las teclas al sistema, y funciona en Wayland.

Ejemplo de ruta:

```json
{
  "punto_de_partida": "spawn",
  "nombre_campo": "sunflower_field",
  "patron_camino": [
    {"tecla": "W", "duracion": 2.5},
    {"tecla": "D", "duracion": 5}
  ],
  "verificacion": null
}
```

## Requisitos

- Linux (probado en Arch con KDE Plasma en Wayland)
- Python 3
- Roblox corriendo con [Sober](https://sober.vinegarhq.org/)
- Permiso sobre `/dev/uinput` para tu usuario y módulo `uinput` cargado

### Permiso para uinput

Crea `/etc/udev/rules.d/99-uinput.rules` con:

```
KERNEL=="uinput", OWNER="tu_usuario", MODE="0660"
```

Luego recarga las reglas con `udevadm`.

## Instalación

```bash
git clone https://github.com/TU_USUARIO/NOMBRE-DEL-REPO.git
cd bss-macro-linux
python -m venv venv
source venv/bin/activate
pip install evdev
```

## Estado del proyecto

- [x] Lectura de rutas desde JSON
- [x] Movimiento por teclado virtual (uinput)
- [x] Liberación segura de teclas al interrumpir
- [ ] Validación de rutas antes de ejecutarlas
- [ ] Verificación de llegada con la pantalla
- [ ] Reintentos y ciclo de farmeo

## Aviso

No está afiliado a Roblox ni a los creadores del juego. Revisa las reglas del juego antes de usarlo.