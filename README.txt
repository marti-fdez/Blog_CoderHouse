
Hola Pedro, en este README te explicamos como hacer correctamente las comprobaciones necesarias para esta entrega.

Empezamos con los Modelos, tenemos 3 modelos:

Profesión, en este modelo tenemos como atributo el nombre de la profesión y su sueldo x mes, como sabemos la profesion debe de ser realizada por una Persona, 
en nuestro caso hemos creado el modelo Blogger, blogger representa cada usuario de nuestro blog, desde trabajadores hasta usuarios/clientes y estos bloggeros
podran tener algún artículo en la web a su nombre, como autores.

Un Blog  debe de tener artículos, el autor de los artículos publicados en el blog debe de ser un Blogger registrado en la web.

TODAS ESTAS RELACIONES SE REPRESENTAN CON FOREIGNS KEYS, TAMBIÉN HAY UN "DIAGRAMA.PNG" PARA CONSULTAR EL DISEÑO  DE LA BASE DE DATOS.

Al tener todos los campos obligatorios, y en dos modelos tenemos FOREIGNS KEYS, debemos seguir un orden de creación de registros en la base de datos.

El orden sería el siguiente:

- Crear una Profesión.
- Crear un Blogger --> relacionar con Profesión existente en la base de datos.
- Crear un Articulo --> relacionar con Blogger existente en la base de datos.

Podemos crear los registros de los modelos nombrados anteriormente en la pestaña administración, donde encontraremos un pequeño menú donde podemos acceder a 
diferentes acciones CRUD.

Como para esta entrega solo se necesitaba de CREATE Y READ, solo estan funcionales la opcion de crear datos y buscar artículos.
Si se crean los registros correctamente arrojarán un mensaje conforme lo ha hecho con éxito.

Los artículos se deberan filtrar por su temática.
Al filtrar nos mostrará información de los todos los articulos con la temática filtrada, sin embargo si no hay una temática con la que se corresponda,
nos mostrará que no ha encontrado nada parecido con esta temática.

Como extra, hay una pestaña de "Artículos" con un artículo de ejemplo, esta ahí temporalmente, tenemos pensado poner ahí como un menú con los artículos 
recomendados y una barra de búsqueda para buscar cualquier articulo del blog y poder acceder a él mediante un botón.

En cuanto a la herencia HTML, todas las páginas heredan al "nav_bar", la barra de navegacíon y el footer con las redes sociales, en github hemos linkado 
nuestro propio repositorio.

 