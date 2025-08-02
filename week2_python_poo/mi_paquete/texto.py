def contar_palabras(texto):
    caracteres = texto.split()
    return len(caracteres)


def invertir_cadena(cadena):
    caracteres = list(cadena)
    caracteres = caracteres[::-1]
    return "".join(caracteres)
