Los **Sets** (conjuntos) son otra estructura de datos fundamental en programación, especialmente útil cuando necesitas manejar colecciones de elementos únicos y realizar operaciones matemáticas de conjuntos. Piénsalos como las bolsas mágicas de las matemáticas: no importa cuántas veces intentes poner el mismo objeto, solo se guardará una vez, y el orden de los objetos no importa.

---
### Sets: Creación
Puedes crear un set de varias maneras en Python:
- **Set vacío:**
    ```python
    mi_set = set()
    ```
    Es importante notar que `{}` crea un diccionario vacío, no un set vacío. Para un set vacío, **siempre usa `set()`**.
- **Con elementos iniciales:** Puedes crear un set a partir de una lista, tupla o cadena de texto, usando llaves `{}` o la función `set()`. Los elementos duplicados se eliminan automáticamente.
    ```python
    # Usando llaves {}
    numeros = {1, 2, 3, 4, 5}
    print(numeros) # Salida: {1, 2, 3, 4, 5}
    
    letras = {'a', 'b', 'c', 'a', 'd'} # 'a' está duplicada
    print(letras)  # Salida: {'a', 'b', 'c', 'd'} (el orden puede variar)
    
    # A partir de una lista
    colores_lista = ["rojo", "azul", "verde", "rojo"]
    colores_set = set(colores_lista)
    print(colores_set) # Salida: {'rojo', 'azul', 'verde'} (el orden puede variar)
    
    # A partir de una cadena de texto (cada carácter es un elemento)
    palabra = "banana"
    letras_palabra = set(palabra)
    print(letras_palabra) # Salida: {'b', 'a', 'n'} (el orden puede variar)
    ```
    Los elementos de un set deben ser **inmutables** (números, cadenas, tuplas). No puedes tener listas o diccionarios directamente como elementos de un set.
---
### Operaciones de Conjuntos
Aquí es donde los sets realmente brillan, ya que ofrecen métodos para realizar las operaciones matemáticas de conjuntos que ya conoces.
#### 1. Unión (cup)
La unión de dos sets es un **nuevo set que contiene todos los elementos de ambos sets**, sin duplicados.
- **Operador `|`:**
    ```python
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    
    union_sets = set_a | set_b
    print(union_sets) # Salida: {1, 2, 3, 4, 5}
    ```
- **Método `union()`:**
    ```python
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    
    union_sets = set_a.union(set_b)
    print(union_sets) # Salida: {1, 2, 3, 4, 5}
    ```
#### 2. Intersección (cap)
La intersección de dos sets es un **nuevo set que contiene solo los elementos que están presentes en ambos sets**.
- **Operador `&`:**
    ```python
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    interseccion_sets = set_a & set_b
    print(interseccion_sets) # Salida: {3, 4}
    ```
- **Método `intersection()`:**
    ```python
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    interseccion_sets = set_a.intersection(set_b)
    print(interseccion_sets) # Salida: {3, 4}
    ```
#### 3. Diferencia (− o setminus)
La diferencia entre dos sets (A - B) es un **nuevo set que contiene los elementos que están en el primer set (A) pero no en el segundo set (B)**.
- **Operador `-`:**
    ```python
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    diferencia_a_menos_b = set_a - set_b
    print(diferencia_a_menos_b) # Salida: {1, 2}
    
    diferencia_b_menos_a = set_b - set_a
    print(diferencia_b_menos_a) # Salida: {5, 6}
    ```
- **Método `difference()`:**
    ```python
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    diferencia_a_menos_b = set_a.difference(set_b)
    print(diferencia_a_menos_b) # Salida: {1, 2}
    ```
#### Operaciones Adicionales Comunes:
- **Diferencia Simétrica (`^` o `symmetric_difference()`):** Elementos que están en uno de los sets, pero no en ambos. Es la unión menos la intersección.
    ```python
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    
    diff_simetrica = set_a ^ set_b
    print(diff_simetrica) # Salida: {1, 2, 4, 5}
    ```
- **Subconjunto (`<=` o `issubset()`):** Comprueba si todos los elementos de un set están contenidos en otro.
    ```python
    set_pequeno = {1, 2}
    set_grande = {1, 2, 3, 4}
    
    print(set_pequeno <= set_grande)    # Salida: True
    print(set_grande.issubset(set_pequeno)) # Salida: False
    ```
- **Superconjunto (`>=` o `issuperset()`):** Comprueba si un set contiene todos los elementos de otro.
    ```python
    set_pequeno = {1, 2}
    set_grande = {1, 2, 3, 4}
    
    print(set_grande >= set_pequeno)    # Salida: True
    print(set_pequeno.issuperset(set_grande)) # Salida: False
    ```
- **Disjuntos (`isdisjoint()`):** Comprueba si dos sets no tienen elementos en común (su intersección es vacía).
    ```python
    set_c = {1, 2}
    set_d = {3, 4}
    set_e = {2, 5}
    
    print(set_c.isdisjoint(set_d)) # Salida: True
    print(set_c.isdisjoint(set_e)) # Salida: False
    ```
---
### ¿Cuándo usar Sets?
Los sets son increíblemente útiles para:
- **Eliminar duplicados:** Si tienes una lista con elementos repetidos y necesitas una colección de elementos únicos.
- **Comprobación rápida de pertenencia:** Saber si un elemento está en una colección es muy eficiente.
- **Operaciones de conjuntos:** Realizar uniones, intersecciones o diferencias entre colecciones de datos.
- **Contar elementos únicos:** Combinado con `len()`, puedes saber cuántos elementos únicos hay en una colección.

---

⬅️[Inicio](../../../../README.md)