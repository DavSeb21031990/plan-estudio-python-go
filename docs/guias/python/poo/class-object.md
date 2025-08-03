## Introducción
La creación de una clase en Python es un proceso directo que comienza con una sintaxis específica. Para declarar una clase en Python, se utiliza la palabra clave class, seguida del nombre que se le asignará a la clase y dos puntos. La sintaxis básica se presenta de la siguiente manera:
```python
class NombreDeLaClase:
    # Contenido de la clase (atributos y métodos)
```

---

## Estructura de una clase vacía (pass)
La forma más sencilla de definir una clase que aún no tiene atributos ni métodos es utilizando la palabra clave pass dentro de su cuerpo. La palabra clave 
pass es una operación nula; no hace nada, pero es necesaria para que Python entienda que el bloque de código de la clase está completo, incluso si está vacío.

```python
class MiClaseVacia:
    pass # Indica que la clase no tiene contenido por ahora
```

Es importante destacar que las definiciones de clases en Python, al igual que las definiciones de funciones (def), son sentencias ejecutables. Esto significa que una clase puede ser definida en cualquier punto del código donde sea legal una sentencia, incluso dentro de una rama condicional (
if) o dentro de una función.

El uso de pass en una clase vacía y la naturaleza ejecutable de las definiciones de clases resaltan la flexibilidad y el dinamismo inherentes a Python. A diferencia de otros lenguajes de programación donde las definiciones de clases son construcciones estáticas que se procesan en tiempo de compilación, en Python, son código que se ejecuta. 

Esta característica permite que las clases sean creadas, modificadas o incluso generadas dinámicamente en tiempo de ejecución, basándose en la lógica del programa. pass no es solo un marcador de posición, sino una declaración legal que permite completar un bloque de código donde se espera contenido, pero aún no se ha proporcionado.

---

## El Constructor `__init__`: Inicializando Objetos
El método `__init__` es una de las características más cruciales en la definición de una clase en Python, ya que desempeña un papel central en la preparación de nuevos objetos.

### Propósito y funcionamiento de `__init__`
El método `__init__` es un método especial en Python que se invoca automáticamente cada vez que se crea una nueva instancia (objeto) de una clase. Su función principal es actuar como el "constructor" de la clase, estableciendo un estado inicial coherente para el objeto recién creado. En esencia, 
`__init__` se utiliza para inicializar los atributos de un objeto, asegurando que cada instancia nazca con un conjunto predefinido de datos.

```python
class Persona:
    def __init__(self):
        print("¡Se ha creado una nueva persona!")

# Al crear un objeto, __init__ se llama automáticamente
p1 = Persona() # Salida: ¡Se ha creado una nueva persona!
```

Este método es fundamental en la Programación Orientada a Objetos, ya que los objetos son entidades con un estado y un comportamiento. Sin `__init__`, cada objeto comenzaría sin atributos definidos, lo que requeriría una asignación manual posterior. Esto sería ineficiente y propenso a errores, especialmente al manejar múltiples objetos.

### El parámetro `self`

El primer argumento de `__init__`, y de hecho de cualquier método de instancia dentro de una clase en Python, es siempre el parámetro `self`. Aunque 
`self` es una convención de nomenclatura fuertemente recomendada y universalmente adoptada en Python, no es una palabra clave reservada del lenguaje; sin embargo, su uso es esencial para la legibilidad y el funcionamiento correcto del código orientado a objetos.

`self` es una referencia a la instancia del objeto que se está creando o sobre el que se está operando. Cuando se llama a un método de instancia (por ejemplo, `objeto.metodo()`), Python pasa implícitamente la propia instancia del objeto como el primer argumento a ese método. Este mecanismo permite que los métodos accedan y modifiquen los atributos específicos de esa instancia particular del objeto.

El parámetro self es el mecanismo por el cual Python vincula una llamada a un método con los datos específicos de una instancia. Cuando se ejecuta `obj.metodo()`, Python lo traduce internamente a `NombreClase.metodo(obj)`. El parámetro `self` captura explícitamente esta referencia `obj`, dejando claro dentro del método que las operaciones se están realizando sobre esta instancia particular. 

Esta elección de diseño refuerza la encapsulación y asegura que cada objeto mantenga su estado único, incluso cuando utiliza métodos compartidos. Es un aspecto fundamental de cómo Python implementa el comportamiento específico de la instancia y lo diferencia de las operaciones a nivel de clase. Comprender `self` es crucial para asimilar el funcionamiento del modelo de objetos de Python y para escribir código orientado a objetos correcto e idiomático, ya que es la piedra angular para gestionar el estado y el comportamiento de las instancias.

### Pasando argumentos al constructor
Para dotar a los objetos de una mayor flexibilidad y personalización al momento de su creación, el método `__init__` puede aceptar argumentos. Estos argumentos se pasan al operador de instanciación de la clase (es decir, cuando se llama a `NombreClase()`) y luego se transfieren directamente al método `__init__` para inicializar los atributos del objeto con valores específicos.

Considérese el siguiente ejemplo con una clase Perro:
```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo de instancia
        self.edad = edad     # Atributo de instancia
        print(f"Se ha creado un perro llamado {self.nombre} de {self.edad} año(s).")

# Se pasan argumentos al instanciar el objeto
ozzy = Perro("Ozzy", 2)       # Salida: Se ha creado un perro llamado Ozzy de 2 año(s).
skippy = Perro("Skippy", 12)  # Salida: Se ha creado un perro llamado Skippy de 12 año(s).
```

En este caso, al crear `ozzy` y `skippy`, se proporcionan los valores para `nombre` y `edad` directamente en la llamada al constructor. El método `__init__` recibe estos valores y los asigna a los atributos `self.nombre` y `self.edad` de cada instancia, respectivamente. Además, es posible definir parámetros con valores por defecto en la firma de `__init__`, lo que permite crear objetos con configuraciones predefinidas si no se proporcionan valores explícitos durante la instanciación.

---

## Atributos: Características de Clases y Objetos
Los atributos son las variables que almacenan el estado de una clase o de sus objetos. En Python, existen dos tipos principales de atributos: los atributos de instancia y los atributos de clase, cada uno con un propósito y un comportamiento distintos.

### Atributos de Instancia: Definición y Acceso
Los atributos de instancia son variables que pertenecen específicamente a una instancia particular de una clase. Esto significa que cada objeto creado a partir de la misma clase tendrá su propia copia de estos atributos, y los valores de estos atributos pueden ser únicos para cada objeto.

La forma más común de definir atributos de instancia es dentro del método `__init__` de la clase, utilizando la sintaxis `self.nombre_atributo = valor`. El uso de `self` asegura que el atributo se asocie a la instancia específica que se está inicializando. Para acceder o modificar un atributo de instancia, se utiliza la notación de punto (.) sobre la instancia del objeto.

```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca    # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

mi_coche = Coche("Toyota", "Corolla")
otro_coche = Coche("Honda", "Civic")

print(mi_coche.marca)    # Salida: Toyota
print(otro_coche.modelo) # Salida: Civic

mi_coche.marca = "Nissan" # Modificación de un atributo de instancia
print(mi_coche.marca)    # Salida: Nissan
```

En este ejemplo, `mi_coche` y `otro_coche` son dos instancias distintas de la clase `Coche`, y cada una tiene sus propios valores para los atributos `marca` y `modelo`. La modificación de `mi_coche.marca` no afecta a `otro_coche.marca`.

### Atributos de Clase: Definición, Acceso y Diferencias con los de Instancia
Los atributos de clase son variables que pertenecen a la clase misma, no a una instancia particular. Esto implica que son compartidos por todas las instancias de esa clase. Los atributos de clase se definen directamente en el cuerpo de la clase, fuera de cualquier método.

Se accede a los atributos de clase utilizando el nombre de la clase (por ejemplo, `NombreClase.atributo_de_clase`). También es posible acceder a ellos a través de una instancia (por ejemplo, `instancia.atributo_de_clase`), pero su modificación a través de una instancia tiene un comportamiento particular y a menudo malinterpretado.

```python
class Animal:
    especie = "Mamífero" # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre # Atributo de instancia

perro1 = Animal("Firulais")
perro2 = Animal("Max")

print(perro1.especie) # Salida: Mamífero (acceso a través de instancia)
print(Animal.especie) # Salida: Mamífero (acceso a través de clase)

Animal.especie = "Vertebrado" # Modificación del atributo de clase
print(perro1.especie) # Salida: Vertebrado (el cambio afecta a todas las instancias)
print(perro2.especie) # Salida: Vertebrado
```

Un aspecto sutil y a menudo confuso en Python es el comportamiento cuando se intenta modificar un atributo de clase a través de una instancia. Cuando se ejecuta una asignación como `instancia.atributo_de_clase = nuevo_valor`, Python no modifica el atributo de clase compartido. En su lugar, crea un nuevo atributo de instancia con el mismo nombre, específicamente para esa instancia, que "oculta" o "sombrea" el atributo de clase original para esa instancia particular. Las subsiguientes referencias a `instancia.atributo_de_clase` recuperarán este nuevo atributo de instancia, mientras que otras instancias y la clase misma seguirán refiriéndose al atributo de clase original. 

Este comportamiento se debe al orden de búsqueda de atributos de Python: primero busca en la instancia, luego en la clase, y finalmente en las clases heredadas. Esta capacidad de "sombreado" es una característica potente pero que puede llevar a errores si no se comprende completamente. Destaca la importancia de la resolución del orden de los atributos y sugiere que los atributos de clase son más adecuados para constantes globales compartidas o valores por defecto, mientras que los atributos de instancia deben utilizarse para el estado único de cada objeto.

La siguiente tabla resume las diferencias clave entre los atributos de instancia y los atributos de clase:
| **Criterio**    | **Atributos de Instancia**                                               | **Atributos de Clase**                                                                 |
|----------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Definición**  | Dentro de `__init__` (usualmente) con `self.`                            | Directamente en el cuerpo de la clase, fuera de cualquier método                      |
| **Alcance**     | Único para cada objeto (instancia)                                       | Compartido por todas las instancias de la clase                                       |
| **Acceso**      | `objeto.atributo`                                                        | `Clase.atributo` o `objeto.atributo`                                                  |
| **Modificación**| `objeto.atributo = valor` (crea un atributo de instancia que "sombrea") | `Clase.atributo = valor` (afecta a todas las instancias)                              |
| **Uso Típico**  | Estado específico de un objeto (ej., nombre, edad)                       | Constantes compartidas, valores por defecto, contadores de instancias                 |

---

## Métodos: Comportamiento de los Objetos
Los métodos son las funciones que se definen dentro de una clase y que permiten a los objetos realizar acciones o manipular sus datos. Son esenciales para definir el comportamiento de los objetos.

### Métodos de Instancia: Definición y Llamada
Los métodos de instancia son funciones que operan sobre los datos (atributos) de un objeto específico. Definen las acciones o el comportamiento que una instancia de una clase puede llevar a cabo. Al igual que el método `__init__`, los métodos de instancia se definen utilizando la palabra clave `def` dentro de la clase, y su primer parámetro debe ser `self`, que hace referencia a la instancia del objeto sobre el que se está operando.

Para llamar a un método de instancia, se utiliza la notación de punto (`.`) sobre la instancia del objeto, seguida del nombre del método y paréntesis `()`.

```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self): # Método de instancia
        print("¡Guau guau!")

    def obtener_informacion(self): # Método de instancia que usa atributos
        print(f"{self.nombre} tiene {self.edad} año(s).")

ozzy = Perro("Ozzy", 2)
ozzy.ladrar()               # Salida: ¡Guau guau!
ozzy.obtener_informacion()  # Salida: Ozzy tiene 2 año(s).
```

Los métodos de instancia no solo acceden a los atributos de la instancia, sino que también pueden modificarlos. Por ejemplo, un método `birthday()` podría incrementar la edad de un perro, encapsulando la lógica de envejecimiento dentro de la clase.

Los métodos de instancia son el mecanismo principal para la encapsulación en Python. Al definir el comportamiento directamente dentro de la clase, los métodos aseguran que el estado interno (atributos) de un objeto se manipule de manera controlada y predecible. 

Esto se alinea con el "Principio de Responsabilidad Única", donde una clase es responsable de gestionar sus propios datos y de proporcionar los métodos necesarios para interactuar con ellos. En lugar de modificar directamente un atributo como `ozzy.edad = 3`, un método como `ozzy.celebrar_cumpleanos()` encapsula la lógica para aumentar la edad, lo que hace que la interfaz del objeto sea más limpia y menos propensa a errores. 

Esto también facilita la integridad de los datos al centralizar cómo se modifican. Esta interacción controlada a través de métodos es fundamental para construir sistemas orientados a objetos robustos y mantenibles, ya que promueve la modularidad, reduce el acoplamiento entre componentes y simplifica la depuración y extensión del código, dado que los cambios en la lógica interna se localizan dentro de la clase.

### Métodos de Clase y Métodos Estáticos (Mención breve)
Además de los métodos de instancia, Python también soporta otros tipos de métodos que tienen propósitos diferentes: los métodos de clase y los métodos estáticos.

**Métodos de Clase:** Se definen utilizando el decorador `@classmethod` y reciben la propia clase (`cls`) como primer argumento, en lugar de la instancia (`self`). Operan sobre los atributos de clase y son útiles para operaciones que afectan a la clase en su conjunto o para proporcionar constructores alternativos que crean instancias de maneras diferentes.

**Métodos Estáticos:** Se definen utilizando el decorador @staticmethod y no reciben ni self ni cls como primer argumento. Son esencialmente funciones utilitarias que están lógicamente relacionadas con la clase pero no necesitan acceder al estado de la instancia ni al estado de la clase.

Si bien los métodos de instancia son el foco principal para definir el comportamiento de los objetos individuales, comprender la existencia y el propósito de los métodos de clase y estáticos es importante para un diseño de clases más avanzado y flexible.

---

## Ejemplos Prácticos y Buenas Prácticas
La aplicación de los conceptos de clases, atributos y métodos se clarifica a través de ejemplos prácticos y la adhesión a las buenas prácticas de codificación.

### Un ejemplo completo de una clase con atributos y métodos
Para consolidar los conceptos discutidos, se presenta un ejemplo completo de una clase Libro que integra un constructor `__init__`, atributos de instancia, un atributo de clase, métodos de instancia y el método especial `__str__` para una representación legible del objeto. Además, se incluyen `docstrings` para documentar el código.

```python
class Libro:
    """
    Representa un libro con título, autor y año de publicación.
    Este docstring resume el comportamiento de la clase.
    """
    # Atributo de clase: compartido por todos los libros
    # Indica el tipo de material por defecto.
    tipo_material = "Impreso"

    def __init__(self, titulo, autor, anio_publicacion):
        """
        Inicializa un nuevo objeto Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            anio_publicacion (int): El año en que se publicó el libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def obtener_resumen(self):
        """
        Devuelve un resumen formateado del libro.
        """
        return f'"{self.titulo}" por {self.autor}, publicado en {self.anio_publicacion}.'

    def es_antiguo(self, anio_limite=2000):
        """
        Verifica si el libro es considerado antiguo basándose en el año de publicación.

        Args:
            anio_limite (int): El año límite para considerar un libro antiguo.
                               Por defecto es 2000.
        Returns:
            bool: True si el libro es anterior al anio_limite, False en caso contrario.
        """
        return self.anio_publicacion < anio_limite

    def __str__(self):
        """
        Devuelve una representación de cadena legible del objeto Libro.
        Este método especial se invoca cuando se utiliza print() o str() en el objeto.
        """
        return self.obtener_resumen()

# Creación de objetos (instanciación)
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("Python Crash Course", "Eric Matthes", 2015)

# Acceso a atributos y llamada a métodos
print(f"Libro 1: {libro1.obtener_resumen()}")
print(f"Tipo de material de Libro 1: {libro1.tipo_material}")
print(f"¿Es '{libro1.titulo}' antiguo? {libro1.es_antiguo()}")

print(f"\nLibro 2: {libro2.obtener_resumen()}")
print(f"Tipo de material de Libro 2: {libro2.tipo_material}")
print(f"¿Es '{libro2.titulo}' antiguo? {libro2.es_antiguo()}")

# Modificación de atributo de clase
print(f"\nTipo de material de la clase Libro (antes de modificar): {Libro.tipo_material}")
Libro.tipo_material = "Digital" # Modifica el atributo de clase
print(f"Tipo de material de la clase Libro (después de modificar): {Libro.tipo_material}")

print(f"\nNuevo tipo de material de Libro 1 (después de modificar la clase): {libro1.tipo_material}")
print(f"Nuevo tipo de material de Libro 2 (después de modificar la clase): {libro2.tipo_material}")

```

### Convenciones de Nomenclatura (PEP 8)
Las directrices clave de nomenclatura para clases y sus miembros incluyen:

- **Clases:** Los nombres de clase deben utilizar CamelCase (también conocido como PascalCase), donde cada palabra comienza con una letra mayúscula y no se utilizan guiones bajos. Ejemplos: `MiClase`, `Persona`, `Rectangle`.

- **Métodos y Atributos (variables):** Los nombres de métodos y atributos deben utilizar snake_case, que consiste en palabras en minúsculas separadas por guiones bajos. Ejemplos: `mi_metodo`, `nombre_atributo`, `anio_publicacion`.

- **Variables "privadas":** Aunque Python no impone una privacidad estricta en los atributos (todos los atributos son accesibles desde fuera de la clase), la convención es utilizar un guion bajo inicial (`_`) para indicar que un atributo o método está destinado para uso interno de la clase. Un doble guion bajo inicial (`__`) se utiliza para el "name mangling", lo que hace que el acceso directo desde fuera de la clase sea más difícil, aunque no imposible, al modificar el nombre del atributo internamente.

La siguiente tabla resume las convenciones de nomenclatura de PEP 8 para elementos comunes de clases:

| **Elemento**             | **Convención de Nomenclatura** | **Ejemplo**         |
|--------------------------|-------------------------------|---------------------|
| Clase                    | CamelCase (PascalCase)        | MiClase, Libro      |
| Método                   | snake_case                    | obtener_resumen     |
| Atributo de Instancia    | snake_case                    | titulo, autor       |
| Atributo de Clase        | snake_case                    | tipo_material       |
| Constante (global)       | UPPER_CASE_SNAKE_CASE         | MAX_VALOR           |

### Documentación con `Docstrings`
Los `docstrings` son cadenas de texto especiales en Python que se utilizan para documentar módulos, funciones, clases y métodos. A diferencia de los comentarios de línea (`#`), los docstrings no son ignorados por el intérprete; en su lugar, se almacenan como metadatos y son accesibles en tiempo de ejecución a través de la función `help()` o el atributo especial `__doc__` de un objeto.

Los `docstrings` se colocan inmediatamente después de la línea de definición de la clase o método, y se encierran en triples comillas, ya sean dobles `"""Docstring"""` o simples `'''Docstring'''`.

Según PEP 257, la guía de estilo para docstrings, el contenido debe ser conciso y descriptivo:
- Para clases, el docstring debe resumir su comportamiento general y, si es aplicable, listar los métodos públicos y las variables de instancia.
- Para métodos (incluido `__init_`_), el docstring debe resumir su comportamiento, documentar sus argumentos, valores de retorno, efectos secundarios y cualquier excepción que pueda generar.
- Para docstrings más largos, se recomienda una línea de resumen seguida de una línea en blanco y luego los detalles adicionales.

El ejemplo de la clase Libro en la sección 6.1 ilustra la implementación de docstrings tanto para la clase como para sus métodos.

---

⬅️[Inicio](../../../../README.md)