Un **valor de retorno** es el resultado o la información que una función envía de vuelta al lugar desde donde fue invocada. Cuando una función ejecuta una sentencia `return`, hace dos cosas principales:
1. **Finaliza la Ejecución de la Función:** El programa sale de la función inmediatamente, y no se ejecuta ninguna línea de código que esté después del `return` dentro de esa función.
2. **Devuelve un Valor:** El valor especificado después de `return` es el "resultado" de la llamada a la función. Este valor puede ser capturado por una variable o usado directamente en una expresión.
### Sintaxis Básica de `return`
```python
def nombre_de_la_funcion(parametros):
    # Código de la función
    # ...
    return valor_a_devolver
```
### Ejemplos Clave
1. **Devolver un Solo Valor:**
    ```python
    def calcular_area_rectangulo(base, altura):
        area = base * altura
        return area # La función devuelve el cálculo del área
    
    # Llamamos a la función y guardamos su valor de retorno en una variable
    area_terreno = calcular_area_rectangulo(10, 5)
    print(f"El área del terreno es: {area_terreno} metros cuadrados.")
    
    # También podemos usar el valor de retorno directamente en una expresión
    print(f"El doble del área es: {calcular_area_rectangulo(8, 4) * 2} metros cuadrados.")
    ```
    _Salida:_
    ```
    El área del terreno es: 50 metros cuadrados.
    El doble del área es: 64 metros cuadrados.
    ```
2. **Devolver Múltiples Valores:** Python es especial porque puedes devolver múltiples valores desde una función. En realidad, los devuelve como una **tupla** (una colección ordenada e inmutable de elementos), pero a menudo puedes desempaquetarlos directamente en varias variables.
    ```python
    def obtener_datos_persona():
        nombre = "Carlos"
        edad = 30
        ciudad = "Quito"
        return nombre, edad, ciudad # Devuelve estos tres valores como una tupla
    
    # Desempaquetamos los valores de retorno directamente en variables
    nombre_persona, edad_persona, ciudad_persona = obtener_datos_persona()
    print(f"La persona se llama {nombre_persona}, tiene {edad_persona} años y vive en {ciudad_persona}.")
    
    # O podemos capturarlos como una tupla única
    datos = obtener_datos_persona()
    print(f"Datos completos: {datos}") # Salida: ('Carlos', 30, 'Quito')
    ```
    _Salida:_
    ```
    La persona se llama Carlos, tiene 30 años y vive en Quito.
    Datos completos: ('Carlos', 30, 'Quito')
    ```
3. **El Significado de `return` sin un valor o la ausencia de `return`:**
    Si una función tiene una sentencia `return` pero no especifica un valor después de ella, o si una función no tiene ninguna sentencia `return` explícita, Python devuelve implícitamente el valor especial **`None`**. `None` es un tipo de dato en Python que representa la ausencia de un valor o un valor nulo.
    ```python
    def solo_imprimir():
        print("Esta función solo imprime.")
        return # Devuelve None implícitamente
    
    def sin_return_explicito():
        print("Esta función tampoco tiene un return explícito.")
    
    resultado1 = solo_imprimir()
    resultado2 = sin_return_explicito()
    
    print(f"El resultado de solo_imprimir es: {resultado1}") # Salida: None
    print(f"El resultado de sin_return_explicito es: {resultado2}") # Salida: None
    
    # Puedes comprobar si un valor es None
    if resultado1 is None:
        print("resultado1 es None.")
    ```
    _Salida:_
    ```
    Esta función solo imprime.
    El resultado de solo_imprimir es: None
    Esta función tampoco tiene un return explícito.
    El resultado de sin_return_explicito es: None
    resultado1 es None.
    ```
4. **`return` para Salir Temprano de una Función:** `return` también se puede usar para salir de una función antes de que llegue al final de su código, a menudo basado en una condición.
    ```python
    def verificar_edad(edad):
        if not isinstance(edad, (int, float)):
            print("Error: La edad debe ser un número.")
            return # Sale de la función si la edad no es numérica
    
        if edad < 0:
            print("Error: La edad no puede ser negativa.")
            return
        elif edad < 18:
            print("Eres menor de edad.")
            return False # Devuelve False para indicar que es menor
        else:
            print("Eres mayor de edad.")
            return True # Devuelve True para indicar que es mayor
    
    print(verificar_edad(20))
    print(verificar_edad(15))
    print(verificar_edad(-5))
    print(verificar_edad("veinte"))
    ```
    _Salida:_
    ```
    Eres mayor de edad.
    True
    Eres menor de edad.
    False
    Error: La edad no puede ser negativa.
    None
    Error: La edad debe ser un número.
    None
    ```
El uso de valores de retorno es lo que permite que las funciones no solo realicen acciones, sino que también produzcan resultados que pueden ser utilizados por otras partes de tu programa, haciendo que tu código sea mucho más flexible y modular.

---

⬅️[Inicio](../../../../README.md)