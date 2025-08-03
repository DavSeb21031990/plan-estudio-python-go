## Fixture
Las fixtures son funciones que proporcionan datos o configuración para tus tests. Son reutilizables y se ejecutan automáticamente.

### Fixtures Básicas
````python
import pytest

@pytest.fixture
def datos_usuario():
    return {
        "nombre": "Juan",
        "edad": 30,
        "email": "juan@example.com"
    }

def test_usuario_valido(datos_usuario):
    assert datos_usuario["nombre"] == "Juan"
    assert datos_usuario["edad"] > 0
````

### Scopes de Fixtures
````python
@pytest.fixture(scope="function")  # Por defecto, se ejecuta en cada test
def fixture_funcion():
    print("Setup por función")
    return "datos"

@pytest.fixture(scope="class")  # Una vez por clase
def fixture_clase():
    print("Setup por clase")
    return "datos_clase"

@pytest.fixture(scope="module")  # Una vez por módulo
def fixture_modulo():
    print("Setup por módulo")
    return "datos_modulo"

@pytest.fixture(scope="session")  # Una vez por sesión completa
def fixture_sesion():
    print("Setup por sesión")
    return "datos_sesion"
````

### Fixtures con Setup y Teardown
````python
@pytest.fixture
def conexion_db():
    # Setup
    conexion = crear_conexion_db()
    print("Conectando a la base de datos")
    
    yield conexion  # Esto es lo que recibe el test
    
    # Teardown
    conexion.close()
    print("Cerrando conexión a la base de datos")

def test_consulta_db(conexion_db):
    resultado = conexion_db.ejecutar("SELECT * FROM usuarios")
    assert len(resultado) > 0
````

### Fixtures Parametrizadas
````python
@pytest.fixture(params=[1, 2, 3])
def numero(request):
    return request.param

def test_numero_positivo(numero):
    assert numero > 0
````

Este test se ejecutará 3 veces, una por cada parámetro

## Fixtures con Configuración
````python
@pytest.fixture
def cliente_api():
    return {
        "base_url": "https://api.ejemplo.com",
        "headers": {"Authorization": "Bearer token123"}
    }

@pytest.fixture
def mock_respuesta():
    class MockRespuesta:
        def __init__(self):
            self.status_code = 200
            self.data = {"mensaje": "éxito"}
        
        def json(self):
            return self.data

````    

---

⬅️ [Inicio](../../../../README.md)