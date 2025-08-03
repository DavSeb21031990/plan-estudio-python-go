Pytest es una maravilla para el testing en Python. Es conocido por su simplicidad, su capacidad de ser altamente extensible y sus mensajes de error claros, lo que lo convierte en la opción favorita de muchos desarrolladores.
Vamos a ver cómo funciona y cómo empezar a hacer pruebas con él.

---
## ¿Cómo Funciona Pytest?
Pytest funciona bajo unos principios muy sencillos pero potentes:
1. **Descubrimiento de Pruebas Automático:** Pytest busca automáticamente archivos que contengan pruebas. Por defecto, busca archivos que empiecen con `test_` o terminen con `_test.py` (ej. `test_mi_modulo.py`). Dentro de estos archivos, busca:
    - Funciones que empiecen con `test_` (ej. `def test_mi_funcion():`).
    - Clases que empiecen con `Test` (ej. `class TestMiClase:`), y dentro de esas clases, métodos que empiecen con `test_`.
2. **Sintaxis Simple (Asserts Nativos):** A diferencia de `unittest` que usa métodos como `assertEqual`, `assertTrue`, etc., Pytest te permite usar la **declaración `assert` nativa de Python**. Esto hace que las pruebas sean mucho más legibles y se sientan más "Pythonic".
    ```python
    # Pytest
    assert 1 + 1 == 2
    
    # unittest
    self.assertEqual(1 + 1, 2)
    ```
    Si un `assert` falla, Pytest te dará un informe muy detallado y útil sobre qué falló y por qué, lo cual es fantástico para depurar.
3. **Fixtures:** Este es uno de los superpoderes de Pytest. Las **fixtures** son funciones especiales que Pytest ejecuta antes de tus pruebas (o grupos de pruebas) para configurar un entorno específico y/o limpiar después de ellas. Son una forma muy potente y reutilizable de manejar la preparación y la limpieza de tus tests, como configurar una conexión a una base de datos, crear objetos de prueba, etc. Se inyectan directamente como argumentos en tus funciones de prueba.
4. **Plugins:** Pytest tiene un ecosistema de **plugins** enorme. Puedes instalar plugins para reportes de cobertura de código, pruebas de rendimiento, integración con Django/Flask, y mucho más. Esto lo hace increíblemente flexible y adaptable a cualquier necesidad.
---
## ¡Manos a la Obra! Cómo Hacer Testing con Pytest
Para empezar, solo necesitas Python y Pytest.
### Paso 1: Instalación
Si aún no lo tienes, instala Pytest usando pip:
```bash
pip install pytest
```
### Paso 2: Tu Primer Test (y la Función a Testear)
Vamos a crear un archivo para nuestra lógica de negocio y otro para nuestras pruebas.
**1. Crea un archivo `calculadora.py`:**
```python
# calculadora.py

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números. Lanza ValueError si el divisor es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
```
**2. Crea un archivo `test_calculadora.py`:** Este archivo contendrá tus pruebas. Recuerda el prefijo `test_`.
```python
# test_calculadora.py
# Importamos las funciones que queremos probar desde nuestro módulo
from calculadora import sumar, restar, multiplicar, dividir
import pytest # No siempre es necesario importarlo directamente, pero es buena práctica si usas sus features

def test_sumar():
    """Prueba la función sumar."""
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(2.5, 3.5) == 6.0

def test_restar():
    """Prueba la función restar."""
    assert restar(5, 3) == 2
    assert restar(10, 0) == 10
    assert restar(0, 5) == -5
    assert restar(-5, -2) == -3

def test_multiplicar():
    """Prueba la función multiplicar."""
    assert multiplicar(2, 3) == 6
    assert multiplicar(5, 0) == 0
    assert multiplicar(-2, 4) == -8
    assert multiplicar(2.5, 2) == 5.0

def test_dividir():
    """Prueba la función dividir."""
    assert dividir(6, 3) == 2
    assert dividir(10, 2) == 5
    assert dividir(5, 2) == 2.5

    # Para probar excepciones (división por cero)
    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        dividir(10, 0)
```
### Paso 3: Ejecutar las Pruebas
Abre tu terminal en el mismo directorio donde guardaste `calculadora.py` y `test_calculadora.py`, y ejecuta:
```bash
pytest
```
Verás una salida similar a esta:
```python
============================= test session starts ==============================
platform ... -- Python ...
plugins: ...
collected 4 items

test_calculadora.py ....                                                 [100%]

============================== 4 passed in ...s ==============================
```
Esto indica que Pytest encontró 4 tests (`test_sumar`, `test_restar`, `test_multiplicar`, `test_dividir`) y todos pasaron.
### Explorando Fallos (y lo útil de Pytest)
Vamos a introducir un error intencionadamente en `test_calculadora.py`:
```python
# Modificando test_sumar para que falle
def test_sumar():
    assert sumar(2, 3) == 6 # ¡Esto es incorrecto! 2 + 3 = 5
    # ...
```
Ahora, vuelve a ejecutar `pytest`:
```bash
pytest
```
La salida ahora será mucho más informativa:
```python
============================= test session starts ==============================
...
collected 4 items

test_calculadora.py F...                                                 [100%]

==================================== FAILURES ==================================
__________________________________ test_sumar __________________________________

    def test_sumar():
>       assert sumar(2, 3) == 6
E       assert 5 == 6
E        +  where 5 = sumar(2, 3)

test_calculadora.py:10: AssertionError
=========================== short test summary info ============================
FAILED test_calculadora.py::test_sumar - assert 5 == 6
========================= 1 failed, 3 passed in ...s =========================
```
¡Mira qué claro! Pytest te dice exactamente qué `assert` falló (`assert 5 == 6`), cuál era el valor esperado (6) y cuál fue el valor real (5), e incluso la línea exacta del fallo. Esto es invaluable para depurar.

---

## Ventajas Clave de Pytest
- **Legibilidad:** Las pruebas son muy fáciles de leer y entender gracias al uso de `assert` nativo.
- **Menos Boilerplate:** No necesitas clases o herencia si no las quieres, lo que significa menos código repetitivo.
- **Potentes Fixtures:** Un sistema de preparación y limpieza de tests flexible y reutilizable.
- **Informes Detallados:** Mensajes de error muy claros que te ayudan a identificar problemas rápidamente.
- **Extensibilidad:** Gran cantidad de plugins para añadir funcionalidades.
- **Compatibilidad:** Puede ejecutar pruebas escritas con `unittest`.
Pytest es una herramienta fantástica que te ayudará a escribir pruebas robustas y mantenibles para tus aplicaciones Python. ¡No dudes en explorarlo y sacarle el máximo partido!

---

⬅️ [Inicio](../../../../README.md)