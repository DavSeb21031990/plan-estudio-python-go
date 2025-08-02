from mi_paquete import calculadora as calc, contar_palabras, invertir_cadena

import requests as req

if __name__ == "__main__":
    respuesta = req.get("https://jsonplaceholder.typicode.com/posts")

    if respuesta.status_code == 200:
        respuesta_json = respuesta.json()
        title = respuesta_json[0]["title"]

        nro_palabras = contar_palabras(title)
        print(f"El título del primer post tiene {nro_palabras} palabras.")
        cadena_invertida = invertir_cadena(title)
        print(f"El título del primer post invertido es: {cadena_invertida}")

        print(f"La suma de 5 + 3 es : {calc.sumar(5, 3)}")
        print(f"La resta de 5 - 3 es : {calc.restar(5, 3)}")

    else:
        print("Error al obtener los datos")
