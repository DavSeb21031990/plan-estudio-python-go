### 1. Creación de Tuplas

Las tuplas se crean de forma similar a las listas, pero utilizando **paréntesis `()`** en lugar de corchetes `[]`. Al igual que las listas, pueden contener elementos de diferentes tipos de datos.
**Ejemplos:**
```python
# Tupla de números enteros
numeros_tupla = (1, 2, 3, 4, 5)
print(f"Tupla de números: {numeros_tupla}")

# Tupla de cadenas
frutas_tupla = ("manzana", "banana", "cereza")
print(f"Tupla de frutas: {frutas_tupla}")

# Tupla mixta
mixta_tupla = (10, "hola", 3.14, False)
print(f"Tupla mixta: {mixta_tupla}")

# Tupla vacía
tupla_vacia = ()
print(f"Tupla vacía: {tupla_vacia}")

# Tupla con un solo elemento (¡nota la coma!)
# Es crucial añadir una coma después del elemento para que Python la reconozca como tupla.
# Sin la coma, Python la interpretaría como una expresión entre paréntesis.
tupla_un_elemento = (1,)
print(f"Tupla de un elemento: {tupla_un_elemento}, tipo: {type(tupla_un_elemento)}")

# Si se omite la coma, no es una tupla:
no_es_tupla = (1)
print(f"Esto no es una tupla: {no_es_tupla}, tipo: {type(no_es_tupla)}")
```
### 2. Acceso a Elementos de una Tupla
El acceso a los elementos de una tupla es idéntico al de las listas. Se utiliza el **índice** del elemento, comenzando desde `0` para el primer elemento. También puedes usar índices negativos para acceder desde el final.
**Ejemplos:**
```python
frutas_tupla = ("manzana", "banana", "cereza", "dátil")

# Acceder al primer elemento (índice 0)
print(f"Primera fruta: {frutas_tupla[0]}") # Salida: manzana

# Acceder al tercer elemento (índice 2)
print(f"Tercera fruta: {frutas_tupla[2]}") # Salida: cereza

# Acceder al último elemento (índice -1)
print(f"Última fruta: {frutas_tupla[-1]}") # Salida: dátil
```
### 3. Slicing (Rebanado) de Tuplas
El slicing también funciona de la misma manera que en las listas, permitiéndote extraer una sub-tupla. La sintaxis `[inicio:fin:paso]` se aplica igual.
**Ejemplos:**
```python
numeros_tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Rebanada desde el índice 2 hasta el 5 (excluido)
print(f"numeros_tupla[2:5]: {numeros_tupla[2:5]}") # Salida: (2, 3, 4)

# Rebanada desde el principio hasta el índice 4 (excluido)
print(f"numeros_tupla[:4]: {numeros_tupla[:4]}") # Salida: (0, 1, 2, 3)

# Rebanada de toda la tupla (crea una copia, aunque sea la misma tupla inmutable)
print(f"numeros_tupla[:]: {numeros_tupla[:]}") # Salida: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Rebanada inversa
print(f"numeros_tupla[::-1]: {numeros_tupla[::-1]}") # Salida: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```
### 4. Inmutabilidad: La Diferencia Clave con las Listas
Aquí es donde las tuplas se distinguen fundamentalmente de las listas. Las tuplas son **inmutables**, lo que significa que **una vez que una tupla ha sido creada, no se puede modificar su contenido**. No puedes añadir, eliminar ni cambiar sus elementos.
**¿Qué implica esto?**
- **No puedes asignar un nuevo valor a un índice específico:**
    ```python
    mi_tupla = (1, 2, 3)
    # mi_tupla[0] = 10 # Esto generaría un TypeError: 'tuple' object does not support item assignment
    # print(mi_tupla)
    ```
- **No tienen métodos para añadir o eliminar elementos:** Métodos como `append()`, `insert()`, `remove()`, `pop()` (que modifican la estructura) no están disponibles para las tuplas.
    ```python
    # mi_tupla.append(4) # Esto generaría un AttributeError
    ```
**Entonces, ¿cómo se "modifica" una tupla?**
Si necesitas cambiar una tupla, la única forma es **crear una tupla completamente nueva** basada en la original y los cambios deseados.
**Ejemplo de "modificación" indirecta:**
```python
original_tupla = (10, 20, 30)
print(f"Tupla original: {original_tupla}")

# Queremos "cambiar" el 20 por 25
# Convertimos la tupla a lista, modificamos la lista, y la volvemos a convertir a tupla
lista_temporal = list(original_tupla)
lista_temporal[1] = 25
nueva_tupla = tuple(lista_temporal)

print(f"Nueva tupla (después de 'modificación'): {nueva_tupla}") # Salida: (10, 25, 30)
```
---
### ¿Cuándo usar tuplas en lugar de listas?
La inmutabilidad de las tuplas les confiere ciertas ventajas y casos de uso específicos:
1. **Seguridad de los datos:** Si tienes una colección de datos que sabes que no debe cambiar durante la ejecución de tu programa (como coordenadas geográficas, fechas fijas, etc.), una tupla garantiza que no se modificará accidentalmente.
2. **Rendimiento:** Las tuplas pueden ser ligeramente más rápidas que las listas en algunas operaciones, ya que su tamaño fijo permite optimizaciones internas.
3. **Claves de diccionario:** Debido a su inmutabilidad, las tuplas pueden usarse como **claves en diccionarios**, algo que las listas no pueden hacer.
    ```python
    coordenadas = {(40.7128, -74.0060): "Nueva York", (34.0522, -118.2437): "Los Ángeles"}
    print(f"Ciudad en Nueva York: {coordenadas[(40.7128, -74.0060)]}")
    ```
4. **Desempaquetado:** Las tuplas son excelentes para desempaquetar valores, por ejemplo, cuando una función devuelve múltiples resultados.
    ```python
    def obtener_nombre_completo():
        return "Juan", "Pérez"
    
    nombre, apellido = obtener_nombre_completo()
    print(f"Nombre: {nombre}, Apellido: {apellido}")
    ```
5. **Iteración:** Aunque son inmutables, puedes iterar sobre los elementos de una tupla de la misma forma que con una lista.

---

⬅️[Inicio](../../../../README.md)