
### En este README explicamos el proyecto final:

# BLOG PYTHON

<p align="center">
<img src="https://github.com/marti-fdez/Entrega1_Fernandez_Cuartero_Torres/blob/99ce287b983549e84eb3bb81a8dacba0c9d0396d/Setup%20-%20Awesome%20Screenshot.gif">
</p>

✔ Video Preview: 
<a href="https://www.awesomescreenshot.com/video/11476136?key=87c5ef9c52fdbaa0c258cfe4d34c9c58" target="_blank">Blog Python Video Preview</a>

✔ Extra: WebSite deployed y subido a servidor
<a href="http://marianc90.pythonanywhere.com/" target="_blank">Blog Python Web</a>

El mismo consta de 3 apps: <br>
BlogApp - La cual consta del modelo Articulo.<br>
Perfiles - La cual corresponde a todo lo relacionado con la administración de los usuarios.<br>
Mesages - Contiene los modelos Chat y Message.<br>

Se realizaron 3 UnitTest que se encuentran en Test.Py de la app BlogApp. Uno verifica la correcta creación de usuarios, otro la creación de Articulos con letras random y el último para comprobar la correcta creación de chat y mensajes.

## Model<br>
## Articulo<br>
En este modelo tenemos como atributos el titulo, subtitulo, cuerpo (RichTextField ya que pertenece al ckEditor), fecha de publicación la cual es seleccionable, imagen, autor y temática.
El autor de los artículos corresponde al user en session, registrado en la web. 
En la page articulos/ podemos encontrar todas las entradas publicadas y buscar en las mismas, mediante la view action_buscar_articulo. CUalquier persona tiene acceso a estas view. En el index podemos encontrar el último artículo publicado. 

Cualquier user registrado, al iniciar sesión puede crear, editar y eliminar entradas, sin importar si es de su autoría, o no. En la sección editar pefil puede modificar sus datos, su avatar y limpiarlo.

TODAS ESTAS RELACIONES SE REPRESENTAN CON FOREIGNS KEYS, salvo en el caso de los avatar que corresponden OneToOne con user.

## Models<br>
## Chat y Messages<br>
Un chat se inicializa en la sesión Mensajería, seleccionando el user con el que se quiere incializar la conversación. Una vez creado el chat, nos permite enviar mensajes. Tambien el usuario puede eliminar el chat, pero no los mensajes.


Atributos de ejemplo para comprobar funcionamiento de creación de datos:

UN ARTICULO DE EJEMPLO:
 - Titulo: Curso de Djando Framework
 - Subtitulo: Django Framework
 - Cuerpo: "Las mayores ventajas de un sistema desarrollado en DJANGO, es que nos permite..."
 - Fecha de Publicacion: "2022-09-10"
 - Temática: "Libre"
 - Autor: User

Los artículos se filtran por su contenido de titulo, subtitulo y cuerpo.
Al filtrar nos mostrará información de los todos los articulos con las palabras encontradas, sin embargo si no hay una palabra con la que se corresponda,
nos mostrará que no ha encontrado nada parecido.

Ejemplo de búsqueda:
 - Palabra = Python = Mostrará la información de los articulo con esa temática.
 - Pablabra = Cualquier cosa = No se ha encontrado ningún artículo con la temática "tematica escrita"

Hay una sección de "Nosotros" con un artículo con nuestra información.

En cuanto a la herencia HTML, todas las páginas heredan al "nav_bar", la barra de navegacíon y el footer con las redes sociales, en github hemos linkado 
nuestro propio repositorio.
Se utilizó un template basado en Bootstrap para el diseño. Y se linkeó adicionalmente a un css con nuestros estilos propios.

Se utilizó la versión de Python 3.10.4.


