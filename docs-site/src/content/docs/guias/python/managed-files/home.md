---
title: "Manejo de Archivos"
description: "Guia para el manejo de archivos"
---

## Apertura y cierre de archivos

La forma más básica es usar `open()`:

```python
# Abrir un archivo
archivo = open('archivo.txt', 'r')
contenido = archivo.read()
archivo.close()  # Importante cerrar el archivo
```

Sin embaro es mejor usar el gestor de contexto `with`, que cierra automáticamente el archivo.

```python
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
# El archivo se cierra automáticamente al salir del bloque
```

## Modos de apertura

Los modos más comunes son:

- `'r'`: Solo lectura (Defecto).
- `'w'`: Escritura (Sobrescribe el archivo).
- `'a'`: Anexar al final del archivo.
- `'x'`: Creación exclusiva (Falla si el archivo ya existe).
- `'b'`: Modo binario (ej: 'rb', 'wb').
- `'t'`: Modo texto (Defecto).
- `'+'`: Lectura y Escritura.

## Métodos de lectura

```python
with open('archivo.txt', 'r') as archivo:
    # Leer todo el archivo
    todo = archivo.read()

    # Leer línea por línea
    archivo.seek(0)  # Volver al inicio
    for linea in archivo:
        print(linea.strip())

    # Leer todas las líneas en una lista
    archivo.seek(0)
    lineas = archivo.readlines()

    # Leer una sola línea
    archivo.seek(0)
    primera_linea = archivo.readline()
```

## Métodos de escritura

```python
# Escribir texto
with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola mundo\n')
    archivo.writelines(['Línea 1\n', 'Línea 2\n'])

# Anexar contenido
with open('archivo.txt', 'a') as archivo:
    archivo.write('Nueva línea\n')
```

## Manejo de errores

```python
try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permisos para acceder al archivo")
except Exception as e:
    print(f"Error inesperado: {e}")
```

## Trabajar con rutas

```python
import os
from pathlib import Path

# Usando os.path (método clásico)
ruta = os.path.join('carpeta', 'subcarpeta', 'archivo.txt')
if os.path.exists(ruta):
    print("El archivo existe")

# Usando pathlib (más moderno)
archivo = Path('carpeta') / 'subcarpeta' / 'archivo.txt'
if archivo.exists():
    with archivo.open('r') as f:
        contenido = f.read()
```

## Codificación de archivos

```python
# Especificar codificación
with open('archivo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

# Manejar errores de codificación
with open('archivo.txt', 'r', encoding='utf-8', errors='ignore') as archivo:
    contenido = archivo.read()
```

## Archivos Json y Csv

```python
import json
import csv

# JSON
datos = {'nombre': 'Juan', 'edad': 30}
with open('datos.json', 'w') as archivo:
    json.dump(datos, archivo, indent=2)

with open('datos.json', 'r') as archivo:
    datos_cargados = json.load(archivo)

# CSV
with open('datos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo, delimiter=';')
    escritor.writerow(['Nombre', 'Edad'])
    escritor.writerow(['Juan', 30])

with open('datos.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
```
