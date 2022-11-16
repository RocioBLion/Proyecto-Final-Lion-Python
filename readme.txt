README.md

Entrega intermedia de nuestro Proyecto final de CoderHouse.
Nuestro Proyecto se trata de una WEB Django con patrón MVT, que incluye tres clases en Models,
Herencia de HTML, un formulario para insertar datos a las clases, un formulario para buscar en 
nuestra BD y un README.md para indicar la ejecución de nuestro Proyecto.

Creado por:
--> Germán Herrera Tello
--> Rocío Belén Lion Sabattins
--> Andrea Ana Regueira


Instrucciones para ejecutar este proyecto
Crear Directorio del proyecto My App

1. Abrir Git Bash para Windows o una terminal para Linux/Unix.

2. Crear directorio de trabajo para el proyecto 

cd
mkdir -p Documents/coder_projects
cd Documents/coder_projects
ls 

-Clonar el proyecto y cambiar de rama
git clone

cd django-coderhouse-project

git checkout

-Abrimos VSCode y una terminal allí

code .

Una vez en VSCode damos Ctrl+j o Terminal/New Terminal
En esa terminal vamos a ejecutar los comandos que detallamos
a continuación. 

3. Crear y activar entorno virtual

(Windows)
python -m venv venv
.\venv\Scripts\activate

(Linux)
python3 -m venv venv
source venv/bin/activate

4. Instalar las dependencias del proyecto

pip install -r requirements.txt

5. Navegamos hacia la carpeta del proyecto my_app

cd my_app

6. Se crean las migraciones con la que trabajará nuestro proyecto de Django

python manage.py makemigrations

7. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django

python manage.py migrate

8. Se crea el super usuario para nuestro proyecto de Django

python manage.py createsuperuser

Ingrese Username
 Email address 
 Password

9. Se levanta el servidor de Django para exponer el servicio por el localhost en el puerto 8000 
   por defecto http://127.0.0.1:8000/

python manage.py runserver

Vamos al navegador y en una pestaña nueva navegamos hacia http://127.0.0.1:8000/smartphone/
o http://localhost:8000/smartphone/ para visualizar nuestro proyecto.

COMANDOS UTILES PARA DJANGO

-Crear proyecto

django-admin startproject <nombre del proyecto>
cd <nombre del proyecto>

-Crear una aplicación en un proyecto

python manage.py startapp <nombre del app>

-Actualizar la base de datos del proyecto con cambios en nuestros modelos

-Se realiza en dos pasos la creación de las migraciones, una por aplicación, y luego se realiza la creación de las tablas en la base de datos.

python manage.py makemigrations
python manage.py migrate

COMANDOS UTILES PARA GIT

Git clone

-Git clone es un comando para descargarte el código fuente existente desde un repositorio remoto (como Github, por ejemplo). 
-Descarga la última versión de tu proyecto en un repositorio y la guarda en tu ordenador

git clone <https://link-con-nombre-del-repositorio>

Git branch

-Creando una nueva rama:

git branch <nombre-de-la-rama>

-Visualización de ramas:

git branch
git branch --list

-Borrar una rama:

git branch -d <nombre-de-la-rama>

Git checkout

-Para cambiarte a una rama existente

git checkout <nombre-de-la-rama>

-Para crear y cambiarte a esa rama al mismo tiempo

git checkout -b <nombre-de-tu-rama>

Git status

-El comando de git status nos da toda la información necesaria sobre la rama actual:

-Si la rama actual está actualizada
-Si hay algo para confirmar, enviar o recibir (pull).
-Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked)
-Si hay archivos creados, modificados o eliminadosstatus

git status

Git add

-Añadir un único archivo:

git add <archivo>

-Añadir todo de una vez:

git add -A
git add .

IMPORTANTE: El comando git add almacena en el stage los cambios de los archivos sin embargo aún no quedan registrados 
en el repositorio hasta que se utilice el comando de confirmación git commit para registrar un punto de control de los cambios.

Git commit

-Git commit establece un punto de control al cual puedes volver más tarde si es necesario. 
Es importante escribir un mensaje para explicar qué hemos desarrollado o modificado en el código fuente.

git commit -m "mensaje de confirmación"

Git push

-Después de haber confirmado tus cambios, el siguiente paso es enviar tus cambios al servidor remoto. 
Git push envía tus commits al repositorio remoto.

git push <nombre-remoto> <nombre-de-tu-rama>
git push origin <nombre-de-tu-rama>

IMPORTANTE: Git push solamente carga los cambios que han sido confirmados con un git commit.

Git pull

-El comando git pull se utiliza para recibir actualizaciones del repositorio remoto.

git pull <nombre-remoto> <nombre-de-tu-rama>
git pull origin master

Git remote

-Sirve para cambiar la dirección url del repositorio que tenemos por origin.

git remote set-url origin <url_de_tu_repositorio_en_GitHub>
git remote set-url origin https://github.com/coder-live-class/django-coderhouse-project.git

COMO SUBIR UN PROYECTO LOCAL A GITHUB.

-Desde la web de github
-Creamos un nuevo repositorio en https://github.com. Le damos nombre, descripción, seleccionamos si va a ser un proyecto publico o privado, 
 y dejamos el check de crear README sin marcar. 
-Le damos a crear repositorio y con esto ya tenemos el repositorio donde alojaremos nuestro proyecto.

-Desde la terminal del equipo donde esta el proyecto que queremos subir a github
-Nos vamos a la carpeta del proyecto y ejecutamos estos comandos.

git init

git add .

git commit -m "first commit"

git remote add origin https://github.com/NOMBRE_USUARIO/NOMBRE_PROYECTO.git

git push -u origin master
