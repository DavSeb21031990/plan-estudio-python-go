---
title: 'Composición de Herencia'
description: 'Guia para Composición de Herencia'
---

El principio "Composición sobre Herencia" es una directriz de diseño fundamental en la Programación Orientada a Objetos (POO) que postula que, en la mayoría de los escenarios, es más ventajoso construir clases complejas combinando objetos de otras clases (composición) en lugar de extender clases existentes (herencia). Este principio surge como una estrategia para mitigar los problemas de rigidez y acoplamiento excesivo que a menudo se asocian con la herencia de implementación.   

## Definición de Composición y su Relación "Tiene un"
La composición se define como un tipo de relación en la que una clase se construye a partir de otras clases, incluyendo instancias de esas clases como sus miembros o atributos. Esta relación se conceptualiza como "Tiene un" (Has-A) o "Es parte de" (Part-Of), por ejemplo, "Una Casa TIENE Habitaciones" o "Una Persona TIENE un Corazón".   

Una característica distintiva de la composición es la fortaleza de esta relación: si el "todo" (la clase que contiene) es destruido, sus "partes" (los objetos componentes) también dejan de existir o de tener sentido en ese contexto. Esta dependencia existencial es lo que la diferencia de la agregación, otro tipo de relación "parte-todo" donde las partes pueden existir independientemente del todo. Por ejemplo, un motor es una parte esencial de un coche; si el coche deja de existir, ese motor en particular deja de tener sentido como parte de ese coche. En contraste, las ruedas de un coche (agregación) pueden existir independientemente del coche.   

## Implementación en Python y Diagrama UML
En Python, la composición se implementa declarando objetos de otras clases como atributos dentro de una clase. Visualmente, en los diagramas de clases UML, la composición se representa con un rombo relleno (diamante sólido) en el lado de la clase "todo" (la clase que contiene), conectado a la clase "parte" (el componente).   

## Ventajas de la Composición
La composición ofrece una serie de ventajas significativas en el diseño de software:

- **Desacoplamiento:** Las clases son menos dependientes entre sí. Esto reduce el impacto de los cambios en una clase sobre otras, ya que las interacciones se realizan a través de interfaces bien definidas en lugar de detalles de implementación internos.   

- **Flexibilidad:** Permite cambiar comportamientos en tiempo de ejecución al intercambiar dinámicamente las instancias de los componentes. Un objeto puede alterar su funcionalidad simplemente sustituyendo uno de sus componentes, lo que ofrece una adaptabilidad superior en comparación con la herencia rígida.   
- **Evita el Problema de la Clase Base Frágil:** Al no depender de los detalles de implementación de una jerarquía de herencia rígida, las modificaciones a una clase componente no afectan inherentemente a las clases que la componen, siempre que la interfaz del componente se mantenga consistente. Esto hace que el sistema sea más robusto y menos propenso a fallos inesperados.   

- **Múltiples Comportamientos sin Herencia Múltiple:** Una clase puede incorporar múltiples comportamientos al contener instancias de diferentes clases que proporcionan esos comportamientos. Esto evita los problemas asociados con la herencia múltiple (como el "problema del diamante"), que aunque Python la soporta, puede ser compleja.   

- **Mayor Legibilidad y Facilidad de Depuración:** El código tiende a ser más claro y los problemas son más fáciles de localizar y depurar, ya que las responsabilidades están mejor segregadas en componentes distintos.   

- **Mejor Escalabilidad:** Facilita la escalabilidad del proyecto de software, ya que los componentes pueden ser desarrollados, probados y mantenidos de forma independiente.   

## Desventajas de la Composición
A pesar de sus ventajas, la composición también presenta algunas desventajas:

- Puede ser un mecanismo "más pesado" y requerir la creación de un mayor número de clases en el diseño inicial.   
- Puede implicar un mayor tiempo de desarrollo inicial debido a la necesidad de diseñar e implementar múltiples componentes.   
- No proporciona polimorfismo de subtipo de forma inherente como la herencia. Sin embargo, esta limitación se supera eficazmente combinando la composición con el uso de interfaces (o clases abstractas en Python).   

## El Problema de la "Clase Base Frágil" (Revisado)
El problema de la "Clase Base Frágil" es un problema arquitectónico fundamental en los sistemas de programación orientada a objetos. Se refiere a la situación en la que modificaciones aparentemente seguras a una clase base pueden causar que las clases derivadas que la heredan funcionen incorrectamente. La causa principal se atribuye a la recursión abierta (despacho dinámico de métodos en `self` en Python) y a la dependencia de las subclases en los detalles de implementación internos de la superclase. Una subclase que sobrescribe un método podría depender de una secuencia interna de llamadas en la superclase que, al ser modificada, rompe la lógica de la subclase sin que esta última haya cambiado su propio código.   

La composición emerge como una solución clave para mitigar este problema. Al no establecer una relación de implementación tan estrecha como la herencia, la composición reduce el acoplamiento directo. En lugar de heredar la implementación, se delega el comportamiento a objetos componentes. Estos componentes pueden ser intercambiados o modificados sin afectar directamente la clase que los contiene, siempre que su interfaz se mantenga consistente. Esto permite una mayor flexibilidad y resiliencia ante los cambios.   

Otras soluciones para el problema de la clase base frágil incluyen declarar métodos final (aunque Python no tiene esta palabra clave, se puede simular), hacer las variables de instancia privadas (usando convenciones de nombres como `__` en Python) y forzar el uso de accesores, o, de manera más amplia, utilizar interfaces para definir contratos de comportamiento (usando el módulo abc en Python).   

## Implicaciones de la Composición
Es importante abordar una posible confusión: algunos afirman que la composición "no es polimórfica". Esta afirmación es una simplificación que puede llevar a malentendidos. Si bien la composición por sí misma no proporciona el polimorfismo de subtipo inherente a la herencia (donde un objeto **Perro** puede ser tratado como un **Animal**), la composición combinada con interfaces (o clases abstractas en Python, usando el módulo abc) es una estrategia muy potente para lograr un polimorfismo flexible. Por ejemplo, un objeto **Coche** puede "tener un" **Motor** que implementa una interfaz `IPowerSource`. Diferentes tipos de motores (eléctricos, de gasolina) pueden implementar esa interfaz de distintas maneras. El Coche delega su comportamiento de "moverse" a su Motor, y el comportamiento resultante es polimórfico a través de la interfaz. Para un arquitecto de software, es vital entender que la composición no impide el polimorfismo, sino que lo habilita de una manera diferente, a menudo más flexible y desacoplada que la herencia pura. Esto permite diseñar sistemas donde los comportamientos pueden ser "plug-and-play" sin la rigidez de una jerarquía de clases de implementación. El principio "Composición sobre Herencia" no significa abandonar el polimorfismo, sino alcanzarlo de una forma más robusta.

La ventaja fundamental de la composición sobre la herencia radica en su capacidad para fomentar un acoplamiento débil entre clases. En la herencia, la subclase está fuertemente acoplada a la implementación de la superclase. Cualquier cambio en los detalles internos de la superclase puede afectar a las subclases, incluso si su interfaz pública no ha cambiado. En contraste, en la composición, la clase que contiene solo depende de la interfaz de sus componentes, no de su implementación interna. El acoplamiento débil es una piedra angular del diseño de software de calidad, ya que reduce la complejidad, facilita el mantenimiento, mejora la reusabilidad y hace que el sistema sea más resistente a los cambios. El "Problema de la Clase Base Frágil" es un síntoma directo del acoplamiento fuerte de la herencia, y la composición es la solución arquitectónica para mitigar este riesgo, promoviendo sistemas más modulares y fáciles de evolucionar.

La tendencia en lenguajes de programación modernos como Kotlin y Julia de hacer las clases y métodos final por defecto, o de promover la composición y las interfaces como alternativa a la herencia de implementación, no es una coincidencia. Es una respuesta directa a los desafíos y problemas prácticos que la herencia ha presentado en el desarrollo de software a gran escala. Esta evolución en el diseño de lenguajes refuerza el principio de "Composición sobre Herencia" como una buena práctica de ingeniería de software. Sugiere que la herencia de implementación debe ser una decisión consciente y justificada, no la opción por defecto para la reutilización de código. Para un arquitecto, esto valida la priorización de la composición para la mayoría de los escenarios de diseño.

## Criterios para Decidir entre Herencia y Composición
La elección entre herencia y composición debe basarse en la naturaleza de la relación que se desea modelar:

- **Herencia:** Se prefiere cuando existe una clara relación "Es un" y se desea compartir una implementación base común, aprovechando el polimorfismo de subtipo de forma directa. Es útil cuando la subclase es una especialización genuina de la superclase y se espera que se adhiera estrictamente al Principio de Sustitución de Liskov.   

- **Composición:** Se prefiere cuando existe una relación "Tiene un" o "Es parte de". Es ideal para construir objetos complejos a partir de partes más simples, para cambiar comportamientos dinámicamente y para reducir el acoplamiento y la fragilidad del sistema. Es la opción preferida cuando la reutilización de código no implica una relación de subtipo estricta.   

- **Una regla general ampliamente aceptada en la arquitectura de software es:** "No uses herencia solo para reutilizar código. En la mayoría de los casos, la razón válida para usar herencia es el polimorfismo". Sin embargo, incluso para el polimorfismo, las interfaces combinadas con composición a menudo ofrecen mayor flexibilidad y un diseño más desacoplado.   

## Ejemplos de Código (Python)
Ejemplo de Composición en Python: Coche que tiene un Motor.
```python
# Clase Motor (componente)
class Motor:
    def __init__(self, tipo="gasolina", potencia=100):
        self.tipo = tipo
        self.potencia = potencia
        self.encendido = False

    def arrancar(self):
        self.encendido = True
        return f"Motor de {self.tipo} arrancado"

    def apagar(self):
        self.encendido = False
        return "Motor apagado"

# Clase Coche (el "todo" que contiene el componente)
class Coche:
    def __init__(self, marca, modelo, tipo_motor="gasolina", potencia_motor=100):
        self.marca = marca
        self.modelo = modelo
        # Composición: un Coche "tiene un" Motor
        self. Motor = Motor(tipo_motor, potencia_motor) 

    def encender(self):
        return f"{self.marca} {self.modelo}: {self.motor.arrancar()}"

    def apagar(self):
        return f"{self.marca} {self.modelo}: {self.motor.apagar()}"

# Uso
if __name__ == "__main__":
    # Creamos un objeto Coche, que internamente crea su Motor
    mi_coche = Coche("Toyota", "Corolla", "gasolina", 150)

    print(mi_coche.encender())
    # Salida: Toyota Corolla: Motor de gasolina arrancado

    print(mi_coche.apagar())
    # Salida: Toyota Corolla: Motor apagado

    # Acceso al componente
    print(f"Tipo de motor: {mi_coche.motor.tipo}")
    # Salida: Tipo de motor: gasolina
```
En este ejemplo, la clase **Coche** contiene una instancia de **Motor** como una de sus propiedades. La vida del objeto **Motor** está fuertemente ligada a la vida del objeto **Coche**, lo que ilustra la relación de composición.   

Ejemplo de Composición para un Sistema de Notificaciones (Python):
```python
# Interfaces (Clases Abstractas) para definir el contrato
from abc import ABC, abstractmethod

class Canal(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class CanalEmail(Canal):
    def enviar(self, mensaje):
        return f"Enviando correo electrónico: {mensaje}"

class CanalSMS(Canal):
    def enviar(self, mensaje):
        return f"Enviando SMS: {mensaje}"

class CanalPushNotification(Canal):
    def enviar(self, mensaje):
        return f"Enviando notificación push: {mensaje}"

class ServicioNotificacion:
    def __init__(self):
        self.canales =
    
    def agregar_canal(self, canal: Canal):
        self.canales.append(canal)
    
    def notificar(self, mensaje):
        resultados =
        for canal in self.canales:
            resultados.append(canal.enviar(mensaje))
        return resultados

# Uso flexible con composición
if __name__ == "__main__":
    servicio = ServicioNotificacion()
    servicio.agregar_canal(CanalEmail())
    servicio.agregar_canal(CanalSMS())
    
    print("--- Notificaciones iniciales ---")
    resultados = servicio.notificar("Sistema actualizado")
    for r in resultados:
        print(r)
    # Salida:
    # Enviando correo electrónico: Sistema actualizado
    # Enviando SMS: Sistema actualizado

    # Fácilmente extensible a nuevos canales en tiempo de ejecución
    servicio.agregar_canal(CanalPushNotification())
    print("\n--- Notificaciones con nuevo canal ---")
    resultados_nuevos = servicio.notificar("Nueva característica disponible")
    for r in resultados_nuevos:
        print(r)
    # Salida:
    # Enviando correo electrónico: Nueva característica disponible
    # Enviando SMS: Nueva característica disponible
    # Enviando notificación push: Nueva característica disponible
```
Este ejemplo demuestra cómo la composición, combinada con clases abstractas (simulando interfaces), permite un sistema de notificación altamente flexible. `ServicioNotificacion` "tiene" una lista de Canales, y puede agregar o cambiar dinámicamente los tipos de canales sin modificar su propia lógica interna. Esto es un claro ejemplo de cómo la composición facilita la extensibilidad y el desacoplamiento, evitando la complejidad que surgiría con la herencia múltiple para combinar diferentes tipos de notificación.   

## Tabla Comparativa: Herencia vs. Composición
La siguiente tabla resume las diferencias clave entre herencia y composición, ofreciendo una referencia rápida para la toma de decisiones de diseño.
| **Característica**               | **Herencia**                                                                                         | **Composición**                                                                                                  |
|----------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Relación**                     | "Es un" (Is-A)                                                                                        | "Tiene un" (Has-A) / "Es parte de" (Part-Of)                                                                      |
| **Concepto Clave**              | Extensión, especialización, jerarquía                                                                | Delegación, construcción a partir de partes                                                                      |
| **Reutilización de Código**      | Sí, compartiendo implementación base                                                                 | Sí, a través de la delegación de responsabilidades                                                                |
| **Acoplamiento**                | Fuerte (acoplamiento de implementación)                                                              | Débil (acoplamiento de interfaz)                                                                                  |
| **Flexibilidad**                | Rígida, cambios en padre afectan hijos                                                               | Flexible, comportamientos cambiables en tiempo de ejecución                                                      |
| **Problema Clase Base Frágil**   | Vulnerable (problema inherente)                                                                      | Mitigado (menos propenso)                                                                                         |
| **Polimorfismo (inherente)**     | Sí (polimorfismo de subtipo directo)                                                                 | No directamente (requiere interfaces/duck typing para polimorfismo)                                               |
| **Cuándo Usar**                 | Cuando la subclase es una verdadera especialización de la superclase y se adhiere al Principio de Sustitución de Liskov. | Cuando se necesita construir funcionalidad a partir de componentes, para mayor flexibilidad y menor acoplamiento. |

La tabla condensa la información clave de ambas técnicas en un formato fácilmente digerible, lo cual es crucial para comprender las diferencias fundamentales y tomar decisiones de diseño. Al listar explícitamente "Cuándo Usar" para cada una, proporciona una guía práctica inmediata, transformando el conocimiento teórico en una herramienta aplicable para el diseño de software. Además, la inclusión de ventajas y desventajas, como el acoplamiento y el problema de la clase base frágil, ayuda a internalizar rápidamente los trade-offs asociados con cada enfoque, reforzando el principio de "Composición sobre Herencia" al visualizar sus beneficios directos.