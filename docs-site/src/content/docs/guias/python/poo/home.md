---
title: 'Programación Orientada a Objetos'
description: 'Guia para Programación Orientada a Objetos'
---

La Programación Orientada a Objetos (POO) es un paradigma de programación, es decir, una forma de estructurar y organizar tu código. En lugar de ver tu programa como una secuencia de instrucciones lógicas que manipulan datos, la POO lo ve como una colección de objetos que interactúan entre sí.

Imagina que estás construyendo una casa. Con un enfoque tradicional, podrías tener instrucciones para "poner ladrillo", "cortar madera", "mezclar cemento". Con POO, piensas en los "ladrillos", las "ventanas", las "puertas" y los "albañiles" como entidades, cada una con sus propias características y habilidades, que se unen para formar la casa.

---

## Clase vs. Objeto
La distinción entre clase y objeto es fundamental en la POO:

Clase: El Plano o Molde

Una clase es como un plano o una plantilla para crear objetos. Define la estructura (qué tipo de información contendrá) y el comportamiento (qué acciones puede realizar) que tendrán todos los objetos de ese tipo.

Piensa en una clase como el plano arquitectónico de una casa. El plano describe cuántas habitaciones tendrá, dónde estarán las ventanas, de qué material serán las paredes, etc. Es una descripción abstracta, no la casa en sí.

No puedes vivir en un plano; solo te dice cómo construir una casa.

Objeto: La Instancia Concreta

Un objeto es una instancia concreta de una clase. Es el "elemento" real que se crea a partir del plano.

Siguiendo el ejemplo, un objeto sería la casa real que se construye a partir del plano arquitectónico. Hay muchas casas que pueden usar el mismo plano, pero cada una es una casa individual, con su propia dirección, su propio color de pintura, y sus propios detalles específicos.

Puedes entrar, vivir y tocar un objeto.

En resumen: La clase es la definición lógica de un tipo de entidad, mientras que el objeto es una ocurrencia física y particular de esa entidad en tu programa.

---

## Atributos y Métodos

Los objetos, creados a partir de clases, tienen dos componentes principales:

Atributos (Propiedades o Características)

Los atributos son las variables que pertenecen a un objeto. Representan las características o el estado de ese objeto en un momento dado.

Volviendo al ejemplo de la casa: si la clase es Casa, sus atributos podrían ser numero_habitaciones (un número entero), color_fachada (una cadena de texto como "blanco"), direccion (otra cadena de texto), tiene_patio (un valor booleano True/False).

Cada objeto Casa que crees tendrá sus propios valores para estos atributos (una casa puede ser 5_habitaciones, roja, Calle Falsa 123; otra puede ser 3_habitaciones, azul, Avenida Siempre Viva 742).

Métodos (Comportamientos o Acciones)

Los métodos son las funciones que pertenecen a un objeto. Representan las acciones o comportamientos que el objeto puede realizar o las operaciones que se pueden hacer con él.

Para la clase Casa, los métodos podrían ser abrir_puerta(), encender_luces(), pintar_fachada(nuevo_color).

Cuando llamas a un método, este opera sobre los atributos del propio objeto. Por ejemplo, mi_casa.pintar_fachada("verde") cambiaría el atributo color_fachada solo de mi_casa, no de otras casas.

---

## ¿Por qué POO?

La POO ayuda a los desarrolladores a:

Organizar el código: Agrupa datos y funciones relacionadas en una sola unidad (la clase/objeto).

Reutilizar código: Una vez que defines una clase, puedes crear tantos objetos como necesites, y las clases pueden heredar características de otras clases.

Modelar el mundo real: Permite representar entidades del mundo real y sus interacciones de una manera más intuitiva.

Mantenibilidad: El código es más fácil de depurar, modificar y extender porque los cambios en una parte del sistema tienen menos probabilidades de afectar a otras partes.