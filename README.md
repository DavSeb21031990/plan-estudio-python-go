# Tareas Semana #2 - Dia Jueves

# Errores
## Problemas con el entorno virtual en windows

### Solución
- Crear un entonro virtual en windows
```shell
# Navegar a la carpeta de trabajo
cd week2_python_poo

# Crear un nuevo entorno virtual
python -m venv poo-env-ws
```

- Activar el entorno virtual
```shell
.\poo-env-ws\Scripts\activate
```
  
## Problemas al ejecutar test dentro del modulo `mi_paquete`

### Solución
- crear el archivo `pytest.ini` en la raiz del proyecto
````ini
[pytest]
minversion = 8.0
addopts = --strict-markers --cov=week2_python_poo/mi_paquete --cov-report=term-missing
testpaths =
    week2_python_poo/mi_paquete/test
pythonpath = .
````

- En los test los `import` se deben usar con la ruta absoluta
````python
from week2_python_poo.mi_paquete.calculadora import sumar, restar
````

- Ejecutar el test desde la raiz
```shell
pytest
```

- Ejecutar el test con covertura
````shell
pytest --cov=mi_paquete
````

- Ejecutar los test con covertura y generar los resultados en formato html
````shell
pytest --cov=mi_paquete --cov-report=html
````