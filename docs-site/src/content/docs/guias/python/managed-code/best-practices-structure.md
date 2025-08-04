---
title: 'Mejores Practicas (Estructura)'
description: 'Guia para Mejores Practicas (Estructura)'
---

## Diseños de Proyectos Estándar: Diseño `src` y Agrupación Lógica
Organizar el código en carpetas separadas para diferentes partes del proyecto es fundamental para la manejabilidad, especialmente en aplicaciones grandes. La estructura del proyecto es una forma de documentación no codificada y un elemento fundamental para la automatización de herramientas y la colaboración, comunicando implícitamente la intención del diseño y facilitando los flujos de trabajo de desarrollo. Una estructura consistente proporciona un mapa predecible. Cuando un nuevo desarrollador se une al equipo, o uno existente revisita código antiguo, una estructura consistente proporciona inmediatamente contexto e indica dónde residen funcionalidades específicas. Esto es una forma de documentación implícita.   

Las estructuras de directorio comunes incluyen:

- **Diseño src:** Un enfoque popular donde el código fuente principal reside en un directorio `src/` (por ejemplo, `raiz_proyecto/src/mi_paquete/`). Esto separa claramente el código del paquete instalable de otros archivos a nivel de proyecto (pruebas, documentación, scripts de construcción).   

- **Agrupación Lógica:** Creación de directorios para funcionalidades distintas (por ejemplo, `modelos/`, `servicios/`, `utilidades/`, `pruebas/`, `docs/`, `bin/` o `scripts/`). Por ejemplo, un "Paquete de Operaciones Matemáticas" podría tener sub-paquetes `básico/` `(para suma, resta)` y `avanzado/` `(para multiplicación, división)`.   

Una buena estructura de carpetas facilita la resolución de problemas y la navegación del código para otros desarrolladores. Esta estructura predecible también facilita el trabajo de las máquinas. Los sistemas de construcción, los ejecutores de pruebas (como `pytest`), los linters y las herramientas de análisis estático a menudo dependen de un diseño de proyecto convencional para funcionar correctamente. Sin él, se necesitarían configuraciones más complejas. La estructura del proyecto no se trata solo de organizar archivos; se trata de organizar información y flujos de trabajo. Es una decisión de diseño que impacta la incorporación, el mantenimiento y la eficiencia de los procesos automatizados (CI/CD). Refleja los principios arquitectónicos del proyecto e influye en la facilidad con la que se pueden agregar nuevas características o corregir errores.

## Adherencia a Convenciones de Nomenclatura Consistentes
Es fundamental seguir las directrices de PEP 8 para las convenciones de nomenclatura: usar guiones bajos para variables y funciones (`snake_case`), y `CapWords` para nombres de clases (`PascalCase`). Se deben usar minúsculas para los nombres de las variables de instancia y evitar nombres demasiado largos o difíciles de recordar. Las variables de instancia no públicas deben usar un solo guion bajo inicial (por ejemplo, `_variable_no_publica`).   

Las convenciones de nomenclatura consistentes son un aspecto crítico de la legibilidad y mantenibilidad del código, actuando como un lenguaje compartido que reduce la carga cognitiva y promueve la colaboración en una base de código. Las guías de estilo como PEP 8 estandarizan cómo se ve y se comporta el código. Cuando todos usan los mismos patrones de nomenclatura, un desarrollador no tiene que adivinar si `mifuncion` es una función o una clase, o si `_variable_interna` está destinada a uso externo. Esta estandarización reduce el esfuerzo mental. En lugar de analizar estilos únicos en cada archivo, el cerebro puede reconocer rápidamente patrones, lo que permite a los desarrolladores centrarse en la lógica en lugar de la sintaxis. También minimiza los errores causados por la mala interpretación de la intención de una variable o función. Las convenciones de nomenclatura son una forma de "API interna" para la base de código. Establecen un vocabulario común y un conjunto de expectativas entre los desarrolladores. Esta comprensión compartida es fundamental para un trabajo en equipo eficaz y garantiza que la base de código pueda ser fácilmente comprendida y modificada por cualquier persona familiarizada con las convenciones, incluso años después.

## Archivos Esenciales del Proyecto: `README.md`, `LICENSE` y `pyproject.toml`
Estos archivos no relacionados con el código son tan vitales como el propio código, sirviendo como el contrato externo y los metadatos del proyecto, lo que permite la detectabilidad, la claridad legal y las compilaciones reproducibles.

### `README.md` 
Proporciona una descripción detallada del paquete, su propósito, cómo instalarlo y usarlo, y a menudo incluye ejemplos. Es crucial para la incorporación de usuarios y la comprensión del proyecto. Sin un `README`, un proyecto es difícil de usar.

### `LICENSE`
Especifica los términos bajo los cuales los usuarios pueden usar, modificar y distribuir el paquete. Es esencial para proyectos de código abierto y aclara los derechos de propiedad intelectual. Sin una `LICENSE`, su estado legal no está claro, lo que dificulta su adopción.

### `pyproject.toml` Un archivo de configuración central y moderno para proyectos Python, utilizado para la configuración del sistema de construcción, metadatos del proyecto (nombre, versión, autores, descripción, dependencias) y configuraciones de herramientas (por ejemplo, Black, Ruff). Simplifica la gestión de dependencias y el empaquetado del proyecto. Sin `pyproject.toml` (o similar), el empaquetado y la gestión de dependencias se vuelven manuales y propensos a errores.

Estos archivos en conjunto forman los "metadatos" y el "contrato externo" del proyecto. Son esenciales para que un proyecto sea detectable, utilizable, legalmente compatible y reproducible en diferentes entornos y por diferentes usuarios. Son parte del aspecto de "empaquetado" de los proyectos Python, transformando una colección de scripts en un producto de software distribuible y mantenible.