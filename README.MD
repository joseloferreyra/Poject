# GESTOR DE LIBROS - BIBLIOTECA

    #### Video Demo: https://youtu.be/EkGY5RoEF-k
    #### Description:

   Este es un programa para llevar un control de los libros que un usuario pudiera tener en su casa; desarrollado en Python utilizando la biblioteca Tkinter para la interfaz gráfica. Este programa tiene como ojetivo controlar los libros que un usuario podria tener en su oficina o su hogar. Permite a los usuarios agregar, editar, eliminar y visualizar los libros que haya cargado.
   El mismo fue desarrolado y probado con asistencia de Inteligencia Artificial Bito.

## Funcionalidad

Las siguientes acciones se encuentran permitidas por el programa:

- **Agregar Libros**: Es posible ingresar nuevos libros con su nombre, autor, género y año de publicación; en el campo de años se contempla la posibilidad de ingresar años en numeros romanos. En los campos de nombre, autor y genero se opto por no condicionar la forma de escribir del usuario y los campos fueron formateados utilizando la funcion Title().
- **Borrar Libros**: Este metodo permite eliminar libros seleccionados de la lista.
- **Editar Libros**: Esta función permite modificar la información de todos o algunos de los campos de informacion de un libro especifico. Para la edicion se depliega una pantalla secundaria con la finalidad de tener visualizacion de los campos que se estan editando en contraste con la lista.  
- **Mostrar Libros**: Representa una lista de todos los libros almacenados en un archivo CSV. Desplegados en forma de lista dentro del formulario principal de la aplicacion.

## Requisitos

Para ejecutar este programa, necesitarás tener instalado lo siguiente:

- **Python**: Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **Bibliotecas de Python**: Este programa utiliza las siguientes bibliotecas que pueden no estar incluidas en la instalación estándar de Python:
  - `tkinter`: Generalmente viene incluido con Python, pero en algunos sistemas puede requerir instalación adicional.
  - `csv`: Esta biblioteca es parte de la biblioteca estándar de Python.
  - Debe existir un archivo llamado library.csv en l directorio de la aplicacion.
  
## Uso

1. Clona o descarga el repositorio en tu máquina local.
2. Navega al directorio donde se encuentra el archivo `main.py`.
3. Ejecuta el programa utilizando el siguiente comando:
   bash
   python main.py

4. Se abrirá una ventana donde el usuario podrá gestionar los libros.

## Mantenimiento

- **Agregar Libros**: Cuando haya completado todos los campos podra hacer click sobre el boton "Agregar Libro".
- **Borrar Libros**: Si desea Borrar algun libro del sistema, debe seleccionar el registro en la lista y dar click en el boton "Borrar Libro".
- **Editar Libros**: Si desea Editar la informacion de un libro podra seleccionar el registro en la lista y hacer click sobre el boton "Editar libro", en la ventana emergente podra modificar, uno o todos los campos del libro luego hacer click sobre el boton "Guardar Cambios"; para que los cambios sean guardados en el archivo csv.

## Contribuciones

Si deseas contribuir al proyecto, siéntete libre de enviar un pull request o abrir un issue para discutir mejoras y nuevas características.
