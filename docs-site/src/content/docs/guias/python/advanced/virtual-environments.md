---
title: 'Entornos Virtuales'
description: 'Guia para entornos virtuales'
---

Los entornos virtuales en Python son espacios aislados que te permiten gestionar las dependencias (bibliotecas y módulos) y la configuración de tus proyectos de forma independiente. Funcionan como "contenedores" o "instalaciones" separadas de Python, cada una con sus propios paquetes, sin afectar la instalación global de Python en tu sistema.

## ¿Por qué son necesarios?

Evitar conflictos de dependencias: Diferentes proyectos pueden requerir versiones distintas de la misma biblioteca. Sin entornos virtuales, instalar una versión para un proyecto podría romper otro. Los entornos virtuales resuelven esto al permitir que cada proyecto tenga su propia versión de las librerías.

Aislamiento de proyectos: Cada proyecto mantiene sus propias dependencias, evitando interferencias con otros proyectos o con la instalación global de Python.

Reproducibilidad: Facilitan la creación de entornos idénticos en diferentes máquinas, lo que asegura que tu código funcione de manera consistente sin importar dónde se ejecute. Puedes compartir un archivo de requisitos (por ejemplo, requirements.txt) para que otros desarrolladores puedan replicar el mismo entorno.

Limpieza del sistema: Evitan la acumulación de paquetes innecesarios en la instalación global de Python, manteniendo tu sistema más ordenado.

Gestión de versiones de Python: Permiten utilizar diferentes versiones de Python para distintos proyectos si es necesario.

## ¿Cómo funcionan?

Cuando creas un entorno virtual, se genera un directorio que contiene una copia aislada del intérprete de Python, pip (el gestor de paquetes de Python) y carpetas para instalar las bibliotecas. Al "activar" un entorno virtual, tu terminal o línea de comandos se configura para usar el Python y los paquetes de ese entorno específico, ignorando la instalación global.

## Herramientas comunes para entornos virtuales:

- `venv`: Es el módulo recomendado y viene incluido en la biblioteca estándar de Python desde la versión 3.3. Es una opción ligera y suficiente para la mayoría de los usuarios.

- `virtualenv`: Una herramienta externa más antigua que funciona con Python 2 y 3, ofreciendo algunas características adicionales.

- `conda`: Un sistema de gestión de paquetes y entornos que va más allá de Python, muy útil especialmente en ciencia de datos.

- `pipenv`: Combina `pip` y `virtualenv` en una sola herramienta con gestión de dependencias mejorada.

- `poetry`: Una herramienta moderna para la gestión de dependencias y empaquetado.

En resumen, los entornos virtuales son una práctica fundamental en el desarrollo con Python para mantener tus proyectos organizados, evitar conflictos y asegurar la reproducibilidad.

---

## Configuración
- Crear un entorno virtual
```python
python -m venv .<name>-venv
```
- Activar un entorno virtual
```python
source .<name>-venv/bin/activate
```
- Desactivar un entorno virtual
```python
deactivate
```