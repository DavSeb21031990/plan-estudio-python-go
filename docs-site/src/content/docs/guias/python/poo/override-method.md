---
title: 'Sobrescritura de Métodos'
description: 'Guia para Sobrescritura de Métodos'
---

La sobreescritura de métodos (conocida también como method overriding o redefinición de métodos) es un concepto fundamental en la Programación Orientada a Objetos que se manifiesta cuando una subclase proporciona su propia implementación para un método que ya ha sido definido en su superclase. El propósito primordial de esta técnica es permitir que la clase hija adapte o personalice el comportamiento heredado para satisfacer sus necesidades específicas, sin modificar la implementación original de la clase base.   

## Reglas y la Anotación `@Override` en Python
En Python, la sobreescritura de métodos es más directa que en otros lenguajes. Simplemente se redefine el método en la subclase con el mismo nombre y firma (parámetros). Python no requiere una anotación explícita como `@Override` (que es común en Java) para indicar la sobreescritura, ya que es implícita. Sin embargo, es una buena práctica de documentación y legibilidad.   

Las reglas clave para la sobreescritura en Python son:

- **Misma Firma:** El método en la subclase debe tener el mismo nombre que el método en la superclase. Aunque Python no impone estrictamente la misma cantidad de parámetros en tiempo de compilación, es una buena práctica mantener la misma firma para preservar el polimorfismo y la sustitución de Liskov.

- **No hay restricciones de static o final:** Python no tiene las palabras clave `static` o `final` para métodos en el mismo sentido que `Java` o `C++`. Todos los métodos pueden ser sobrescritos por defecto, a menos que se utilicen mecanismos más avanzados como `metaclases` o `decoradores` para restringir este comportamiento.

## Uso de `super()` para Extender el Comportamiento
La función `super()` se utiliza dentro de un método sobrescrito en la subclase para invocar el método original de la superclase. Esta práctica es particularmente útil cuando se desea añadir funcionalidad adicional en la subclase, pero al mismo tiempo se quiere preservar o extender el comportamiento original del método de la superclase. Permite una combinación de la lógica heredada con la lógica especializada de la subclase, creando un comportamiento que es una extensión del original.   

## Vinculación Dinámica (Runtime Polymorphism)
La sobreescritura de métodos es un ejemplo clave de vinculación dinámica (o late binding). Esto significa que el intérprete no puede determinar qué implementación de un método se ejecutará hasta el tiempo de ejecución del programa. La decisión se toma basándose en el tipo real del objeto en ese momento, lo que permite una flexibilidad significativa en el comportamiento del programa.   

## Diferencia con Sobrecarga de Métodos (Method Overloading)
**Es fundamental distinguir la sobreescritura de la sobrecarga de métodos (method overloading):** La sobrecarga permite definir múltiples métodos con el mismo nombre pero con diferentes firmas (es decir, distinto número o tipo de argumentos) dentro de la misma clase o en una jerarquía de herencia. La vinculación de llamadas a métodos sobrecargados se resuelve en tiempo de compilación (vinculación estática). Python no soporta la sobrecarga de métodos en el mismo sentido que **Java** o **C++** (es decir, no se pueden tener dos métodos con el mismo nombre y diferente número de parámetros en la misma clase); en su lugar, se utilizan valores por defecto para los parámetros o un número variable de argumentos `(*args, **kwargs)`.   

La sobreescritura, en cambio, ocurre en el contexto de la herencia, donde una subclase redefine un método que tiene la misma firma que uno de su superclase. La vinculación de llamadas a métodos sobrescritos se resuelve en tiempo de ejecución (vinculación dinámica).   

## Implicaciones de la Sobreescritura de Métodos
La sobreescritura de métodos es el mecanismo habilitador directo para el polimorfismo en tiempo de ejecución. Sin la capacidad de una subclase para proporcionar su propia implementación de un método heredado, no sería posible que objetos de diferentes tipos (pero que comparten una superclase común) respondan al mismo "mensaje" (llamada a método) de maneras distintas. Esta capacidad es fundamental para la flexibilidad y extensibilidad del código en la POO, ya que permite que un programa interactúe con una colección de objetos de una superclase de manera uniforme, mientras que cada objeto individualmente ejecuta su comportamiento especializado. Esta es la esencia del principio "una interfaz, muchas implementaciones".

Además, el uso de `super()` dentro de un método sobrescrito no es solo una característica sintáctica, sino que representa un patrón de diseño importante: la extensión o el aumento del comportamiento, en lugar de su reemplazo completo. Permite que la lógica fundamental definida en la superclase se mantenga, mientras que la subclase añade o modifica aspectos específicos. Este enfoque fomenta un diseño más robusto y menos propenso a errores. Si una subclase simplemente reemplaza el método de la superclase sin invocar super(), corre el riesgo de duplicar lógica o, peor aún, de omitir pasos cruciales que la superclase manejaba. La invocación a super() facilita la creación de jerarquías donde las subclases construyen sobre la base de la superclase de manera incremental y segura.

Ejemplos de Código (Python)
```python
# Superclase
class Vehículo:
    def arrancar(self):
        print("El vehículo está arrancando.")

# Subclase
class Coche(Vehículo):
    def arrancar(self): # Sobreescritura implícita
        print("El coche está arrancando.")

# Uso
if __name__ == "__main__":
    mi_vehiculo = Vehículo()
    mi_coche = Coche()

    mi_vehiculo.arrancar() # Salida: El vehículo está arrancando.
    mi_coche.arrancar()    # Salida: El coche está arrancando. (Método sobrescrito)
```
En este caso, cuando se llama a `arrancar()` en un objeto Coche, se ejecuta la implementación específica de Coche, no la genérica de `Vehiculo`.   

Ejemplo con `super()` (Python): Extender el comportamiento de `arrancar()`.
```python
# Superclase (misma que antes)
class Vehículo:
    def arrancar(self):
        print("El vehículo está arrancando.")

# Subclase
class Coche(Vehículo):
    def arrancar(self):
        super().arrancar() # Llama al método arrancar() de la superclase Vehiculo
        print("El coche está listo para arrancar y salir a la carretera.")

# Uso
if __name__ == "__main__":
    mi_coche = Coche()
    mi_coche.arrancar()
    # Salida:
    # El vehículo está arrancando.
    # El coche está listo para arrancar y salir a la carretera.
```
Aquí, `super().arrancar()` asegura que la lógica de inicialización del Vehiculo se ejecute antes de que el Coche añada su propia lógica especializada.   

Ejemplo con `Animal.hacer_sonido()` (Python):
```python
# Superclase
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico de un animal"

# Subclase Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

# Subclase Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Uso
if __name__ == "__main__":
    perro = Perro()
    gato = Gato()
    print(perro.hacer_sonido()) # Salida: Guau!
    print(gato.hacer_sonido()) # Salida: Miau!
```
Este ejemplo ilustra cómo diferentes subclases pueden proporcionar implementaciones únicas para un método heredado, demostrando la personalización del comportamiento.   

Ejemplo con NotImplementedError (Python):
```python
class MetodoPago:
    def procesar_pago(self, cantidad):
        # Este método debe ser sobrescrito por las subclases
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Procesando un pago de {cantidad} con tarjeta de crédito."

class PayPal(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Procesando un pago de {cantidad} con PayPal."

# Uso
if __name__ == "__main__":
    tarjeta = TarjetaCredito()
    paypal = PayPal()
    print(tarjeta.procesar_pago(100))
    print(paypal.procesar_pago(150))

    # Intentar usar MetodoPago directamente lanzaría un NotImplementedError
    # metodo_generico = MetodoPago()
    # print(metodo_generico.procesar_pago(50))
```
En este ejemplo, `NotImplementedError` se utiliza para indicar que procesar_pago en MetodoPago es un método que debe ser implementado por las subclases, similar a un método abstracto en otros lenguajes.  