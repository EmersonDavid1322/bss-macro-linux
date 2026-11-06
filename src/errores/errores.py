class ErrorMacro(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class ErrorTecla(ErrorMacro):
    def __init__(self, tecla, campo, paso):
        self.tecla = tecla
        self.campo = campo
        self.paso = paso
        mensaje = f"Tecla invalida: '{tecla}' en la ruta del campo: '{campo}' en el paso: '{str(paso)}'"
        super().__init__(mensaje)