## Configuración

Para generar cobertura de código (code coverage) en los tests de Python usando pytest, necesitas usar el plugin
pytest-cov, que es una herramienta basada en coverage.py.

### Instala las herramientas necesarias
````shell
pip install pytest pytest-cov
````

### Configuraciones si se esta usando entornos virtuales
Si estás usando un entorno virtual, haz esto dentro del entorno.

#### Configuración en pytest.ini
````ini
ini[tool:pytest]
addopts = --cov=mi_proyecto --cov-report=html --cov-report=term-missing
testpaths = tests
````

#### Configuración en pyproject.toml
````toml
toml[tool.pytest.ini_options]
addopts = "--cov=mi_proyecto --cov-report=html --cov-report=term"
testpaths = ["tests"]

[tool.coverage.run]
source = ["mi_proyecto"]
omit = [
    "*/tests/*",
    "*/venv/*",
    "*/__pycache__/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
]
````

### Ejecutar cobertura con pytest
````shell
pytest
````
O manualmente sin pytest.ini:
````shell
pytest --cov=mi_paquete --cov-report=term-missing
````
- `--cov=mi_paquete`: genera cobertura solo de ese paquete

- `--cov-report=term-missing`: muestra qué líneas no fueron cubiertas
### Ver reporte HTML (opcional)
Para obtener un reporte visual en HTML:
````shell
pytest --cov=mi_paquete --cov-report=html
````
Esto crea una carpeta `htmlcov/` con un archivo `index.html`. Ábrelo en tu navegador para revisar visualmente qué líneas están cubiertas y cuáles no.

### Otras formas de reporte
| Opción                  | Resultado                                            |
| ----------------------- | ---------------------------------------------------- |
| `--cov-report=term`     | Reporte resumen en consola                           |
| `--cov-report=annotate` | Archivos fuente con comentarios de cobertura         |
| `--cov-report=xml`      | XML para integración con CI/CD (ej. GitHub, Jenkins) |

### Establecer un porcentaje minimo de cobertura para pasar los test
````shell
pytest --cov=mi_paquete --cov-fail-under=90
````

---

⬅️ [Inicio](../../../../README.md)