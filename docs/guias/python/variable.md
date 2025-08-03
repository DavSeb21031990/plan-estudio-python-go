## Definición

Imagina una variable como una **caja con una etiqueta**. Dentro de esa caja, puedes guardar cualquier tipo de
información: un número, un texto, una lista de cosas, etc. La **etiqueta** es el nombre que le das a la caja (la
variable), y es la forma en que Python sabe qué información estás intentando usar.

## Funcionamiento

Python es un lenguaje de **tipado dinámico y fuerte**. Esto significa dos cosas importantes con respecto a las
variables:

1. **Tipado Dinámico:** No necesitas decirle a Python qué tipo de dato vas a guardar en una variable (si será un número
   entero, un texto, etc.). Python lo averigua automáticamente cuando le asignas un valor.
    ```python
   nombre = "Juan"  # Python sabe que 'nombre' es un texto (string)
   cantidad = 10    # Python sabe que 'cantidad' es un número entero (integer)
    ```
   Además, puedes **cambiar el tipo de dato** que guarda una variable en cualquier momento:
    ```python
   x = 10      # x es un entero
   x = "Hola"  # Ahora x es un texto
    ```
2. **Tipado Fuerte:** Una vez que Python sabe el tipo de dato, no te permitirá hacer operaciones ilógicas con tipos
   diferentes sin una conversión explícita.
    ```python
   numero = 5
   texto = "Hola"
   # print(numero + texto) # Esto daría un error, no puedes sumar un número y un texto directamente
   print(str(numero) + texto) # Aquí sí funciona porque convertimos el número a texto
    ```

## Asignación de valores

Para asignar un valor a una variable, usas el signo de igual ` = `. Este signo se conoce como **operador de asignación
**.

```python
mi_variable = "Este es un valor"
precio_unitario = 25.50
es_activo = True
```

## Valores como referencias

En Python, cuando asignas un valor a una variable, en realidad la variable **no contiene directamente el valor**, sino
que **referencia** (apunta a) un objeto en la memoria que contiene ese valor.

```python
a = [1, 2, 3]  # 'a' apunta a la lista [1, 2, 3] en la memoria
b = a  # 'b' también apunta a la misma lista que 'a'
b.append(4)  # Modificamos la lista a través de 'b'
print(a)  # Salida: [1, 2, 3, 4] -> 'a' también se ve afectada porque apuntan al mismo objeto
```

Si quisieras una copia independiente, tendrías que hacer una copia explícita (por ejemplo, `b = a[:]` para listas).

## Ejemplos

```python
# Creando variables de diferentes tipos
nombre_usuario = "Alicia"  # String (cadena de texto)
saldo_cuenta = 1500.75  # Float (número decimal)
edad = 28  # Integer (número entero)
es_premium = True  # Boolean (verdadero/falso)
lista_compras = ["leche", "pan", "huevos"]  # List (lista de elementos)
datos_personales = {"nombre": "Carlos", "ciudad": "Quito"}  # Dictionary (diccionario clave-valor)

# Imprimiendo el valor de las variables
print("Nombre de usuario:", nombre_usuario)
print("Saldo disponible:", saldo_cuenta)
print("Edad:", edad)
print("Es usuario premium:", es_premium)
print("Primer item en la lista de compras:", lista_compras[0])
print("Ciudad de Carlos:", datos_personales["ciudad"])

# Reasignando un valor
saldo_cuenta = saldo_cuenta - 200
print("Nuevo saldo:", saldo_cuenta)

# Asignación múltiple
x, y, z = 10, 20, 30
print(f"Valores: x={x}, y={y}, z={z}")
```

---

⬅️[Inicio](../../../README.md)