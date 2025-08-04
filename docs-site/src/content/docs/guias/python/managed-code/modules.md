---
title: 'Módulos'
description: 'Guia para modulos'
---

## Analogia 
Piensa en un **módulo** como un solo archivo de Python (`.py`) que contiene código relacionado, como funciones, clases y variables. Es como tener diferentes cajones en una cómoda; cada cajón (módulo) guarda un tipo específico de ropa (código) para que no todo esté en un solo montón desordenado.

## Definición y Propósito Central: Encapsulación de Código en Archivos Únicos
Un módulo de Python es, en su esencia, un archivo único que contiene definiciones y sentencias de Python, generalmente guardado con la extensión `.py`. Estos módulos sirven como contenedores para organizar funciones, clases y variables relacionadas, lo que permite dividir el código en piezas más pequeñas y manejables. El propósito principal de un módulo es habilitar la reutilización del código: las definiciones creadas en un módulo pueden ser importadas y utilizadas en otros módulos o scripts, eliminando la necesidad de copiar y pegar código repetidamente.

Los módulos actúan como la unidad atómica de encapsulación lógica y reutilización dentro de un proyecto Python, sirviendo como la primera capa de abstracción para gestionar la complejidad. Un archivo `.py` se convierte en un módulo cuando está diseñado para ser importado, lo que implica un contrato: el módulo proporciona ciertas funcionalidades, y los consumidores las importan. Esta capacidad de importación es lo que lo convierte en un componente reutilizable. Al encapsular la lógica relacionada (funciones, clases, variables) dentro de un único archivo, se crea una unidad autocontenida que puede ser fácilmente utilizada en otras partes del programa. Cada módulo posee su propio espacio de nombres, lo que previene conflictos de nombres al combinar código de diferentes fuentes. Esta es la base de la programación modular en Python, el primer paso para descomponer un problema grande en partes más pequeñas y manejables, lo que contribuye directamente a la facilidad de gestión y mantenimiento del código.   

## ¿Por qué usar Módulos?
1. **Organización del Código:** Divide tu programa en archivos más pequeños y manejables, cada uno con una responsabilidad específica. Esto es vital para proyectos grandes.
2. **Reusabilidad:** Puedes definir funciones o clases una vez en un módulo y luego importarlas y usarlas en cualquier otro script de Python. Esto evita la repetición de código.
3. **Mantenibilidad:** Si necesitas cambiar una función, solo tienes que modificarla en un lugar (su módulo original), y todos los scripts que la usen verán el cambio automáticamente.
4. **Colaboración:** Permite que varios desarrolladores trabajen en diferentes partes de un mismo proyecto sin pisarse el código.

## Creación de un Módul
Crear un módulo es tan sencillo como crear un archivo de texto con extensión `.py`.

**Paso 1: Escribe tu código en un archivo.**

Vamos a crear un módulo simple llamado `matematicas.py` que contendrá algunas funciones matemáticas básicas:
```python
# matematicas.py

PI = 3.14159 # Una variable global en el módulo

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta el segundo número del primero."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide el primer número por el segundo. Maneja división por cero."""
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# Este código solo se ejecuta si el módulo se corre directamente
# y no cuando se importa en otro archivo
if __name__ == "__main__":
    print("Este es el módulo de matemáticas.")
    print(f"El valor de PI es: {PI}")
    print(f"La suma de 5 y 3 es: {sumar(5, 3)}")
    print(f"La división de 10 por 2 es: {dividir(10, 2)}")
    print(f"Intentando dividir por cero: {dividir(10, 0)}")
```

**Nota sobre `if __name__ == "__main__":`**: Este es un patrón común en Python. El código dentro de este bloque solo se ejecuta cuando el archivo `.py` se ejecuta directamente (por ejemplo, `python matematicas.py`). Si el archivo se importa como un módulo en otro script, este bloque de código no se ejecuta, lo cual es útil para pruebas o ejemplos de uso del módulo.