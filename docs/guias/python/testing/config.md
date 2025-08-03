## Configuración básica para realizar test
Se debe realizar la siguiente configuración para poder realizar los test sin inconvenientes con sus imports o ubicación de sus test.

## Estructura recomendada
Se recomienda basarse en esta estructura de directorios para no tener inconvenientes en la ejecución de los test.
````markdown
plan-estudio-python-go/
├── pytest.ini
├── requirements.txt
├── week2_python_poo/
│   ├── __init__.py
│   ├── mi_paquete/
│   │   ├── __init__.py
│   │   ├── calculadora.py
│   │   └── test/
│   │       ├── __init__.py
│   │       └── test_calculadora.py
└── ...

````

## Crear archivo `pytest.ini` en la raíz (plan-estudio-python-go/)
````ini
[pytest]
minversion = 8.0
addopts = --strict-markers --cov=week2_python_poo/mi_paquete --cov-report=term-missing
testpaths = 
    week2_python_poo/mi_paquete/test
pythonpath = .
````
🔎 Esto asegura que:

- Se tomen los tests desde week2_python_poo/mi_paquete/test 
- Las rutas relativas funcionen correctamente 
- Se ejecute coverage solo sobre el código que importa (mi_paquete)
- No tengas que agregar el proyecto manualmente al **PYTHONPATH**

## Importaciones dentro de los tests
En `test_calculadora.py`, usa importación absoluta desde la raíz lógica definida en `pytest.ini`:
````python
import pytest
from week2_python_poo.mi_paquete.calculadora import sumar, restar

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (1, 1, 2)
])
def test_suma(a, b, expected):
    assert sumar(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 0),
    (1, 1, 0)
])
def test_resta(a, b, expected):
    assert restar(a, b) == expected
````

## Ejecutar tests correctamente
Desde el directorio raíz del proyecto (plan-estudio-python-go/), ejecuta:
````shell
pytest
````
👉 No necesitas pasar argumentos adicionales. Todo lo configuraste en `pytest.ini`.

---

⬅️ [Inicio](../../../../README.md)