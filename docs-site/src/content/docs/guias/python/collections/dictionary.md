---
title: 'Diccionarios'
description: 'Guia para Diccionarios'
---

Los diccionarios en programación son una estructura de datos muy útil y versátil. Piénsalos como un armario con compartimentos etiquetados, donde cada etiqueta es una "clave" y lo que guardas dentro de cada compartimento es un "valor". A diferencia de las listas (que usan números como índices), los diccionarios te permiten usar cualquier cosa inmutable (como cadenas de texto, números o tuplas) como clave para acceder a tus datos.
Vamos a desglosar cada punto:
### Diccionarios: Creación, acceso por clave, adición/modificación/eliminación de entradas.
#### 1. Creación de Diccionarios
Puedes crear un diccionario de varias maneras:
- **Diccionario vacío:**
    ```python
    mi_diccionario = {}
    otro_diccionario = dict()
    ```
- **Con elementos iniciales:** Se usan pares `clave: valor` separados por comas, dentro de llaves `{}`.
    ```python
    persona = {
        "nombre": "Ana",
        "edad": 30,
        "ciudad": "Madrid"
    }
    
    productos = {
        101: "Laptop",
        102: "Mouse",
        103: "Teclado"
    }
    ```
    También puedes crear un diccionario a partir de una lista de tuplas (pares clave-valor):
    ```python
    datos = [("uno", 1), ("dos", 2), ("tres", 3)]
    numeros = dict(datos)
    # numeros será {'uno': 1, 'dos': 2, 'tres': 3}
    ```
#### 2. Acceso por Clave
Para obtener el valor asociado a una clave, utilizas la clave entre corchetes `[]` después del nombre del diccionario.
```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

print(persona["nombre"])   # Salida: Ana
print(persona["edad"])     # Salida: 30

# Si la clave no existe, se generará un error KeyError
# print(persona["pais"]) # Esto daría un error
```
Para evitar el error `KeyError` cuando no estás seguro si una clave existe, puedes usar el método `get()`:
```python
print(persona.get("ciudad")) # Salida: Madrid
print(persona.get("pais"))   # Salida: None (valor por defecto si la clave no existe)
print(persona.get("pais", "Desconocido")) # Salida: Desconocido (puedes especificar un valor por defecto)
```
#### 3. Adición de Entradas
Para añadir un nuevo par `clave: valor`, simplemente asigna un valor a una nueva clave entre corchetes `[]`:
```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

persona["ocupacion"] = "Ingeniera"
print(persona)
# Salida: {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'}
```
#### 4. Modificación de Entradas
Si la clave ya existe, asignar un nuevo valor a esa clave modificará el valor existente:
```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

persona["edad"] = 31
print(persona)
# Salida: {'nombre': 'Ana', 'edad': 31, 'ciudad': 'Madrid'}

persona["ciudad"] = "Barcelona"
print(persona)
# Salida: {'nombre': 'Ana', 'edad': 31, 'ciudad': 'Barcelona'}
```
#### 5. Eliminación de Entradas
Puedes eliminar entradas de un diccionario de varias maneras:
- **Usando `del`:** Elimina un par `clave: valor` específico.
    ```python
    persona = {
        "nombre": "Ana",
        "edad": 30,
        "ciudad": "Madrid"
    }
    
    del persona["ciudad"]
    print(persona)
    # Salida: {'nombre': 'Ana', 'edad': 30}
    ```
    Si la clave no existe, `del` generará un `KeyError`.
- **Usando `pop()`:** Elimina un par `clave: valor` y devuelve el valor asociado a la clave. Esto es útil si necesitas usar el valor que estás eliminando.
    ```python
    persona = {
        "nombre": "Ana",
        "edad": 30,
        "ciudad": "Madrid"
    }
    
    edad_eliminada = persona.pop("edad")
    print(f"La edad eliminada es: {edad_eliminada}") # Salida: La edad eliminada es: 30
    print(persona)
    # Salida: {'nombre': 'Ana', 'ciudad': 'Madrid'}
    ```
    `pop()` también permite un segundo argumento opcional para un valor por defecto si la clave no se encuentra (evitando un `KeyError`):
    ```python
    ciudad_eliminada = persona.pop("pais", "No encontrado")
    print(f"País eliminado: {ciudad_eliminada}") # Salida: País eliminado: No encontrado
    ```
- **Usando `clear()`:** Elimina todas las entradas del diccionario, dejándolo vacío.
    ```python
    persona = {
        "nombre": "Ana",
        "edad": 30,
        "ciudad": "Madrid"
    }
    
    persona.clear()
    print(persona)
    # Salida: {}
    ```
### Métodos comunes (keys, values, items)
Estos métodos son muy útiles para iterar o trabajar con las claves, los valores o ambos a la vez en un diccionario.
#### 1. `keys()`
Este método devuelve un objeto tipo "vista" que muestra una lista de todas las claves en el diccionario. Puedes convertirlo fácilmente a una lista si lo necesitas.
```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

claves = persona.keys()
print(claves)         # Salida: dict_keys(['nombre', 'edad', 'ciudad'])
print(list(claves))   # Salida: ['nombre', 'edad', 'ciudad']

# Puedes iterar directamente sobre las claves:
print("\nClaves del diccionario:")
for clave in persona.keys():
    print(clave)
```
#### 2. `values()`
Este método devuelve un objeto tipo "vista" que muestra una lista de todos los valores en el diccionario.
```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

valores = persona.values()
print(valores)         # Salida: dict_values(['Ana', 30, 'Madrid'])
print(list(valores))   # Salida: ['Ana', 30, 'Madrid']

# Puedes iterar directamente sobre los valores:
print("\nValores del diccionario:")
for valor in persona.values():
    print(valor)
```
#### 3. `items()`
Este método devuelve un objeto tipo "vista" que muestra una lista de tuplas, donde cada tupla contiene un par `(clave, valor)` del diccionario. Es ideal para iterar sobre ambos al mismo tiempo.
```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

elementos = persona.items()
print(elementos)        # Salida: dict_items([('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Madrid')])
print(list(elementos))  # Salida: [('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Madrid')]

# Ideal para iterar sobre clave y valor simultáneamente:
print("\nClaves y valores del diccionario:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```
### ¿Cuándo usar diccionarios?
Los diccionarios son perfectos cuando necesitas:
- **Asociar información:** Por ejemplo, la edad de una persona, el precio de un producto, la configuración de una aplicación.
- **Buscar datos rápidamente:** El acceso por clave es muy eficiente.
- **Almacenar datos semiestructurados:** Como la información de un perfil de usuario o las propiedades de un objeto.