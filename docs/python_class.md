# Python 2021

La página del curso es: https://cursos.lcg.unam.mx/course/view.php?id=78

Markdown Cheatsheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

El Path de trabajo en mi computadora es: /home/dianaoaxaca/Dropbox/Python_2021/

Instalar Git

```bash
sudo apt-get install git
```

## Sesión 1

### Markdown

#### Textos

_italica_  = un asterisco bordenado la palabra o _ undersore _

**bold**    = doble asterísco

~~Scratch~~  = doble viborita

Numeraciones:

1. Lista uno

* también con asterísco

  - Con guión medio

  + Con +

#### URLs

```
[Texto](URL)
[Texto](URL "Título del link")
[Texto](Path a un archivo o repositorio)

```

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

#### Imágenes

```
![alt text](liga o path)## alt text, palabras claves de la imágen
```

![prueba de imagen](/home/dianaoaxaca/Dropbox/Weissella Manuscrito a Revision/ParaFrontiers/Revision Frontiers/Figures/Figure3r.tiff)

Para ver la lista de directorios d etrabajo uso `ls` , y para saber cual es mi directorio de trabajo el comando `pwd` 

Mi script es el siguiente:

```shell
ls
pwd
cd data
mkdir tmp
```

#### Tablas

```
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:| # El número de guines es el ancho de la columna
#Los dos puntitos : indican la alineación
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
```

### Git y Github

* Estándares de codificación: PEP8 para python https://google.github.io/styleguide/

* Utilizar estándares de nombrado

* Buenas prácticas:

* * Encabezados de programas
* Documentación interna (esta función hace el calcuñlo de tal forma y se ejecuta asi)
  * Nombrado adecuado de variables y métodos/funciones
* Nombrado adecuado de los programas
  * Organización adecuada del código (Estructura de directorios (Carpetas y archivos))
* Compartir el código con mis compañeros para obtener retroalimentación.
  
* Git no controla los cabios en archivos binarios
* Control de versiones
  * **Forma manual:** Constituído por dos dígitos, versiones primarias y secundarias (X, Y). En cambios menores cambia la versión secundaria y cuando los cambios son mayores o drásticos, cambia la versión primaria.
  * **Forma automática**: Git es una herramienta que ayuda a llevar el seguimiento de las versiones de archivos, controla los cambios que se realicen y crea difrentes versiones.
    * Git de manera local
      * sólo yo puedo tener cceso al código
      * Puedo controlar en mi computadora los cambios que haga
      * Mi software se vuelve sólo de uso personal
    * Git+GitHub
      * Permite trabajar conjuntamente una idea

**Git local, configuración**

```
sudo apt-get install git
git --version
git config --global user.name "tuNombre"
git config --global user.email "hoaxacadiana@gmail.com
git config --list
```

**Estructura del directorio de trabajo**

```shell
docs # archivos de documentación 

lib #Librerias y dependencias

src #Programas Python

test #archivos para pruebas
```

**Iniciar un repositorio**

```shell
git init # inicializar Git
ls -la #Revisar el repositorio
git status # comprobar el repositorio
git log #Muestra todo el historial de commits
ver antes un ls -la
y después ya hay un .git
ls -l .git/

copiar un archivo a src
cp docs/data-git/data-git/reverse-complement.py ./src/
cd src
##Agregar un cambio
git add reverse-complement.py
##Guardar el cambio -m indica agregar el mensaje, -a permite un mensaje más largo (revisar si si es -a)
git commit -m "Primer commit para agregar el archivo reverse-complement.py"
```

## Sesión 2

Continuación de Git

```shell
git commit --amend -m "Mensaje" #Para cambiar elmensaje

###ejercicio
#Modificar el archivo reverse-complemente agregando la palabra FILENAME al final de la línea de Usage
#ver las diferencias
git diff #Muestra las diferencias
git add reverse-complement.py #Agregar el cambio
git commit -m "se modificó el archivo reverse-complement.py" #Guardar el cambio con su mensaje


#Ejercicio 2
1.Modificar de nuevo el archivo reverse-complement.py agreegando en la última linea sequence.txt
2.Ver las diferencias con git diff
3. Ejecutar el comando:
git diff --staged reverse-complement.py ##Staged compara el área de preparación contra el repositorio, y git diff solito, evalua los cambios del archivo en el área de preparación sin tomar en cuenta el repositorio final.

git log #Lista todos los commits realizados en el repositorio, en orden cronológico inverso
git log -N #N indica el número de commits que queremos obtener, debe ser un número git log -2
git log --oneline # Despliega la información resumida

git status #Indica el estado de los archivos que pueden ser controlados por Git, o aquellos que ya están controlados pero se han modificado. 
git status -u #identificar archivos sin seguimiento

#Ejercicio3
1. Agregar un archivo .md a la carpeta docs
2. verificar el status
3. Verificar el estatus de los archivos sin seguimiento
4. Agregar los cambios del archivo reverse-complemnt.py y de la incorporación del archivo.md
5. Guardar los cambios

#Ejercicio 4
1. Modificar el archivo reverse-complement.py
2. Agregar al directorio src el archivo sequence.txt
3. Agregar los cambios al área de preparación
4. Hacer commit de ambos archivos


```

Además de hacer referencia al commit por el identificador también podemos hacerlo por medio del indicador `HEAD`

`HEAD`  Cada commit representa un head 

```shell
1. Editar el archivo reverse-complement.py agregando un nuevo autor
nano reverse-complement.py
2. Comparar el archivo con la versión anterior
git diff HEAD reverse-complement.py

hay cosas que no entendí aquí

git show HEAD~1 reverse-complement.py # muestra la información de la cabecera o identificador 1
```

Como restaurar una versión

Recuperar versión estable/funcionable

Cambié algo y ahora ya no funciona mi código

Reviso fechas y commits para regresar a una versión en particular

```shell
git checkout #Permite recuperar versiones anteriores indicando el commit al que queremos volver

```

Como modificar el mensaje de un comió en particular

1. identificar el commit  donde actualizaremos el mensaje

   `git log --oneline`

## Sesión 3

gitignore Para controlar y poner las reglas del repositorio

```
#Escribir un archivo oculto llamado .gitignore

```

```
git status --ignored -u # ver la lista de archivos que estamos ignorando
```

ignorar todos los archivos de una extención (*.data), excepto uno (final.data)

```
*.data
!final.data
```

Conectar el repositorio local con web

```
git remote add origin
```

Sincronizarlos

```
git remote -v
```

Todo lo que vive en master local, llevatelo a web

```
git push origin master

#Pide usuario y contraseña
```

Ahora del web actualizarlo a local

```
git pull origin master
```

