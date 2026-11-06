from src.errores.errores import ErrorTecla

def identificar_tecla(tecla_texto, listado):
    return listado.get(tecla_texto)

def validar_teclas(teclas_permitidas, teclas_ingresadas, campo_ruta):
    for indice, paso in enumerate(teclas_ingresadas):
        if identificar_tecla(paso["tecla"], teclas_permitidas) is None:
            raise ErrorTecla(tecla=paso["tecla"], campo=campo_ruta, paso=indice+1)