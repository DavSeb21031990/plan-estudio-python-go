## Parametrización: Tests Dinámicos
La parametrización te permite ejecutar el mismo test con diferentes datos de entrada.

### Parametrización Básica
````python
import pytest

@pytest.mark.parametrize("entrada,esperado", [
    (2, 4),
    (3, 9),
    (4, 16),
    (-2, 4),
])
def test_cuadrado(entrada, esperado):
    assert entrada ** 2 == esperado
````

### Parametrización con Múltiples Parámetros
````python
@pytest.mark.parametrize("a,b,resultado", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0),
    (0, 100, 100),
])
def test_suma_parametrizada(a, b, resultado):
    assert suma(a, b) == resultado
````

### Parametrización con IDs Personalizados
````python
@pytest.mark.parametrize("email,valido", [
    ("test@example.com", True),
    ("invalid-email", False),
    ("@example.com", False),
    ("test@", False),
], ids=["email_valido", "sin_arroba", "sin_usuario", "sin_dominio"])
def test_validacion_email(email, valido):
    assert es_email_valido(email) == valido
````

### Parametrización Anidada
````python
@pytest.mark.parametrize("navegador", ["chrome", "firefox"])
@pytest.mark.parametrize("dispositivo", ["desktop", "mobile"])
def test_compatibilidad(navegador, dispositivo):
    # Se ejecutará 4 veces: todas las combinaciones
    resultado = probar_compatibilidad(navegador, dispositivo)
    assert resultado is True
````

### Parametrización con Objetos Complejos
````python
python@pytest.mark.parametrize("usuario", [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Carlos", "edad": 30, "activo": False},
    {"nombre": "María", "edad": 35, "activo": True},
])
def test_procesar_usuario(usuario):
    resultado = procesar_usuario(usuario)
    assert "nombre" in resultado
    assert resultado["procesado"] is True
````

⬅️ [Inicio](../../../../README.md)