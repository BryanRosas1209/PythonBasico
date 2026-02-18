Investigación: Sistemas de Gestión de Bases de Datos Relacionales
1. El Lenguaje Universal: SQL

SQL significa Structured Query Language (Lenguaje de Consulta Estructurado). Es el lenguaje que se usa para comunicarse con las bases de datos relacionales. Con SQL podemos crear tablas, guardar información, hacer consultas, actualizar datos y eliminarlos cuando sea necesario.

Aunque SQL es un estándar internacional, cada motor de base de datos tiene pequeñas diferencias en su forma de usarlo. Esto pasa porque cada empresa agrega funciones propias para mejorar el rendimiento o añadir características especiales.

Por ejemplo, MySQL, Oracle Database, Microsoft SQL Server y PostgreSQL utilizan SQL, pero cada uno tiene comandos o funciones que pueden cambiar un poco. A estas diferencias se les llama “dialectos” de SQL. La base es la misma, pero cada sistema tiene su propio estilo.

2. El Rol del Motor: Base de Datos vs SGBD

Muchas veces se confunden estos dos conceptos, pero no son lo mismo.

Una Base de Datos es simplemente el conjunto de datos organizados. Por ejemplo, una colección de tablas con información de clientes, productos o ventas.

Un Sistema de Gestión de Bases de Datos (SGBD o DBMS) es el programa que permite crear, administrar y controlar esa base de datos. Es el que se encarga de:

Controlar quién puede acceder a la información.

Proteger los datos.

Hacer copias de seguridad.

Optimizar las consultas.

Evitar errores o pérdida de información.

En pocas palabras:
La base de datos es la información.
El SGBD es el software que permite manejar esa información.

3. El Caso de SQLite

SQLite es diferente a los demás porque se considera “serverless” (sin servidor). Esto significa que no necesita un servidor funcionando aparte. La base de datos se guarda en un solo archivo dentro de la aplicación.

¿Dónde se usa más?

SQLite es muy común en:

Aplicaciones móviles (especialmente en Android).

Aplicaciones de escritorio.

Navegadores web.

Dispositivos pequeños o sistemas integrados.

Se usa mucho porque es liviano, fácil de implementar y no necesita configuración complicada. Es perfecto para aplicaciones que funcionan de manera local o que no tienen muchos usuarios al mismo tiempo.

¿Por qué no sirve para una red social grande?

Una red social con millones de usuarios necesita:

Muchas conexiones al mismo tiempo.

Servidores distribuidos.

Alta disponibilidad.

Capacidad de manejar grandes volúmenes de datos.

SQLite no está diseñado para soportar miles o millones de usuarios simultáneamente. Funciona mejor para proyectos pequeños o aplicaciones individuales. Para sistemas grandes se suelen usar motores como MySQL, PostgreSQL o Oracle Database, que están preparados para entornos más exigentes.

4. La Historia de MariaDB

MariaDB tiene una relación directa con MySQL.

MySQL originalmente no pertenecía a Oracle. Primero fue desarrollado por MySQL AB, luego fue comprado por Sun Microsystems, y más tarde Oracle Corporation compró Sun Microsystems. Así fue como MySQL pasó a ser propiedad de Oracle.

Esto generó preocupación en la comunidad de software libre porque Oracle también tenía su propio sistema de base de datos comercial. Muchas personas temían que MySQL dejara de ser completamente abierto o que su desarrollo cambiara de rumbo.

Por esa razón, el creador original de MySQL impulsó la creación de MariaDB como una bifurcación (fork) del proyecto. La idea era mantener el código abierto, seguir mejorándolo y asegurar que fuera totalmente compatible con MySQL.

Actualmente, MariaDB es una alternativa muy utilizada y en muchos casos puede reemplazar directamente a MySQL sin grandes cambios.