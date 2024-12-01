# Proyecto Django Blog

Este es un proyecto basado en Django para gestionar un blog. A continuación, te explicamos los pasos para poner en funcionamiento el proyecto en tu entorno local.

## Requisitos

- **Python 3.x** instalado.
- **Django** (se instalará en un entorno virtual).

## Pasos para configurar el proyecto

### 1. Clona el repositorio

Primero, clona el repositorio del proyecto:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_directorio_del_repositorio>

2. Crea un entorno virtual
Es importante que uses un entorno virtual para gestionar las dependencias del proyecto. Para crear uno, ejecuta los siguientes comandos:

En Windows:
python -m venv venv

En Linux/MacOS:
python3 -m venv venv

3. Activa el entorno virtual
Una vez creado el entorno virtual, actívalo:

En Windows:
.\venv\Scripts\activate

En Linux/MacOS:
source venv/bin/activate

4. Instala las dependencias
Con el entorno virtual activado, instala Django y cualquier otra dependencia del proyecto:

pip install django

5. Configura la base de datos
El siguiente paso es aplicar las migraciones para crear las tablas necesarias en la base de datos. Ejecuta los siguientes comandos:

python manage.py migrate

6. Ejecuta el servidor
Ahora, puedes ejecutar el servidor de desarrollo de Django:

python manage.py runserver

7. Accede a la aplicación
Abre tu navegador y ve a la siguiente dirección:

http://127.0.0.1:8000/blog

Ahí podrás ver la página de inicio del blog.

Notas adicionales
Si deseas crear un superusuario para acceder al panel de administración, puedes ejecutar:

python manage.py createsuperuser
Para detener el servidor, presiona Ctrl + C en la terminal.

¡Eso es todo! Ahora puedes trabajar en el proyecto de Django y hacer tus cambios. Si tienes algún problema, no dudes en abrir un issue en el repositorio.
