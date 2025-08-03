## 1. Argumentos Predeterminados (Default Arguments)

Los argumentos predeterminados te permiten especificar un **valor por defecto para un parámetro** cuando defines una función. Si el llamador de la función no proporciona un argumento para ese parámetro, se utiliza el valor por defecto. Si se proporciona, el valor por defecto se ignora.
### ¿Por qué usarlos?
- **Flexibilidad:** Hacen que las funciones sean más fáciles de usar, ya que no siempre tienes que proporcionar todos los argumentos.
- **Valores Comunes:** Son útiles cuando un parámetro tiene un valor que se usa la mayoría de las veces.
- **Compatibilidad:** Puedes agregar nuevos parámetros a funciones existentes sin romper el código que ya las usa.
### Sintaxis y Reglas
```python
def saludar(nombre, saludo="Hola"): # 'saludo' tiene un valor predeterminado
    print(f"{saludo}, {nombre}!")

# Uso:
saludar("Ana")            # Usa el valor predeterminado para 'saludo'
saludar("Pedro", "¡Qué tal") # Sobreescribe el valor predeterminado
```
_Salida:_
```
Hola, Ana!
¡Qué tal, Pedro!
```
**Regla Importante:** Los parámetros con valores predeterminados **siempre deben ir después de los parámetros sin valores predeterminados (posicionales)** en la definición de la función.
```python
# CORRECTO:
def ejemplo(param1, param2, param_defecto1="def1", param_defecto2="def2"):
    pass

# INCORRECTO (dará un error de sintaxis):
# def ejemplo_error(param_defecto1="def1", param1):
#    pass
```

---
## 2. `*args` (Argumentos Posicionales Variables)
A veces, no sabes de antemano cuántos argumentos posicionales le vas a pasar a una función. Aquí es donde entra `*args`.
- El `*` antes de `args` (puedes usar cualquier nombre después del `*`, pero `args` es la convención) significa que la función puede aceptar **cero o más argumentos posicionales**.
- Dentro de la función, `args` se convierte en una **tupla** que contiene todos los argumentos posicionales que se le pasaron.
### ¿Por qué usarlos?
- **Flexibilidad Extrema:** Permite que una función maneje un número variable de entradas sin tener que definir un montón de parámetros individuales.
- **Agregación de Datos:** Útil cuando necesitas operar sobre una colección de elementos que se pasan como argumentos separados.
### Ejemplo
```python
def sumar_todo(*numeros): # 'numeros' capturará todos los argumentos posicionales
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todo(1, 2))             # Output: 3
print(sumar_todo(10, 20, 30, 40)) # Output: 100
print(sumar_todo())                 # Output: 0 (una tupla vacía)
```
En este ejemplo, `*numeros` se convierte en una tupla:
- En la primera llamada: `numeros` es `(1, 2)`
- En la segunda llamada: `numeros` es `(10, 20, 30, 40)`
- En la tercera llamada: `numeros` es `()`
---

## 3. `**kwargs` (Argumentos de Palabra Clave Variables)

De manera similar a `*args`, `**kwargs` te permite pasar un **número variable de argumentos de palabra clave** (keyword arguments) a una función.
- El `**` antes de `kwargs` (al igual que con `args`, puedes usar otro nombre, pero `kwargs` es la convención) significa que la función puede aceptar **cero o más argumentos de palabra clave**.
- Dentro de la función, `kwargs` se convierte en un **diccionario** donde las claves son los nombres de los argumentos de palabra clave y los valores son sus respectivos valores.
### ¿Por qué usarlos?
- **Configuración Flexible:** Ideal para funciones que pueden aceptar muchas opciones de configuración, pero no todas son necesarias cada vez.
- **Lectura Clara:** Los argumentos de palabra clave son muy legibles, ya que especifican su propósito por nombre.
- **Metadatos:** Útil para pasar información adicional o metadatos que una función podría necesitar.
### Ejemplo
```python
def mostrar_perfil(nombre, **detalles_adicionales): # 'detalles_adicionales' capturará el resto
    print(f"Nombre: {nombre}")
    for clave, valor in detalles_adicionales.items():
        print(f"{clave.replace('_', ' ').title()}: {valor}")

mostrar_perfil("Elena", edad=28, ciudad="Madrid", profesion="Ingeniera")
print("---")
mostrar_perfil("Juan", pais="México")
```
_Salida:_
```
Nombre: Elena
Edad: 28
Ciudad: Madrid
Profesion: Ingeniera
---
Nombre: Juan
Pais: México
```
En la primera llamada, `detalles_adicionales` es `{'edad': 28, 'ciudad': 'Madrid', 'profesion': 'Ingeniera'}`. En la segunda llamada, `detalles_adicionales` es `{'pais': 'México'}`.

---
## Combinando Argumentos Predeterminados, `*args` y `**kwargs`
Puedes usar todos estos conceptos juntos en la misma definición de función, pero hay un **orden estricto** en el que deben aparecer los parámetros:
1. **Parámetros posicionales obligatorios**
2. **Parámetros con valores predeterminados**
3. **`*args` (argumentos posicionales variables)**
4. **`**kwargs` (argumentos de palabra clave variables)**
```python
def configurar_juego(nombre_jugador, nivel_dificultad="Normal", *logros, **configuracion_extra):
    print(f"Jugador: {nombre_jugador}")
    print(f"Dificultad: {nivel_dificultad}")

    if logros: # Si la tupla de logros no está vacía
        print("Logros obtenidos:")
        for logro in logros:
            print(f"- {logro}")

    if configuracion_extra: # Si el diccionario de configuración no está vacío
        print("Configuración adicional:")
        for clave, valor in configuracion_extra.items():
            print(f"  {clave}: {valor}")

print("--- Juego 1 ---")
configurar_juego("Alice")

print("\n--- Juego 2 ---")
configurar_juego("Bob", "Dificil", "Matamarcianos", "Explorador", fps=60, modo_oscuro=True)

print("\n--- Juego 3 ---")
configurar_juego("Charlie", fps=30) # Aquí 'fps' se interpreta como **kwargs, no *args
                                    # Si pones 'Charlie', 30, fps=30, el 30 sería dificultad y fps=30 sería kwargs
```
_Salida:_
```python
--- Juego 1 ---
Jugador: Alice
Dificultad: Normal

--- Juego 2 ---
Jugador: Bob
Dificultad: Dificil
Logros obtenidos:
- Matamarcianos
- Explorador
Configuración adicional:
  fps: 60
  modo_oscuro: True

--- Juego 3 ---
Jugador: Charlie
Dificultad: Normal
Configuración adicional:
  fps: 30
```
Comprender y utilizar `*args` y `**kwargs` te da un poder increíble para escribir funciones muy flexibles y reutilizables en Python. Son especialmente útiles al construir bibliotecas o APIs donde no puedes prever todas las formas en que los usuarios querrán llamar a tus funciones.

---

⬅️[Inicio](../../../../README.md)