1. ¿Para qué sirven los getters y setters?

En programación orientada a objetos, una de las ideas principales es que los datos de un objeto no deberían modificarse sin ningún tipo de control. Los getters y setters existen justamente para eso: controlar cómo se accede y cómo se modifica la información interna de un objeto.

Un getter es un método que permite obtener el valor de un atributo. Un setter permite cambiar ese valor, pero no de cualquier manera, sino aplicando reglas si es necesario.

¿Por qué esto es importante? Porque a veces no queremos que alguien cambie un dato directamente sin validarlo primero. Por ejemplo, podríamos necesitar verificar que un número esté dentro de cierto rango, que un texto no esté vacío, o incluso que antes de cambiar un valor se ejecute algún proceso adicional.

En resumen, los getters y setters ayudan a mantener el control y la coherencia de los datos, aplicando el principio de encapsulamiento, que básicamente significa proteger la información interna del objeto y manejarla de forma segura.


2. ¿A qué se refiere self en un método de una clase?

self es una forma de referirse al objeto específico que está usando el método en ese momento.

Cuando defines una clase, estás creando una especie de plantilla. Pero cuando creas un objeto a partir de esa clase, cada objeto tiene sus propios datos. Entonces, cuando un método necesita acceder a esos datos, necesita saber de qué objeto estamos hablando. Ahí entra self.

Podríamos decir que self es como decir “este objeto en particular”. Es la manera en que Python permite que los métodos trabajen con los atributos y comportamientos del objeto que los está ejecutando.

No es una palabra reservada obligatoria (podría llamarse distinto), pero por convención siempre se usa self porque deja claro que estamos hablando del objeto actual.

En pocas palabras:
self conecta los métodos con los datos del objeto que los está usando.


3. ¿Qué es super()?

super() tiene que ver con la herencia, que es cuando una clase toma características de otra. En este contexto, super() permite acceder a métodos de la clase padre desde la clase hija.

Cuando una clase hereda de otra, muchas veces queremos reutilizar lo que ya está hecho en la clase base en lugar de reescribirlo. super() nos facilita eso. Nos permite llamar al comportamiento original y, si queremos, ampliarlo o complementarlo.

Por ejemplo, una clase hija puede usar super() para ejecutar primero lo que hace la clase padre y luego agregar algo propio. Así se evita duplicar código y se mantiene una estructura más ordenada.

En resumen, super() sirve para aprovechar y extender el comportamiento heredado, manteniendo el código más limpio y reutilizable.