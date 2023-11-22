Prueba técnica
==============

Pasos para instalar el entorno
------------------------------

1. Crear un entorno virtual para el proyecto usando Python3

``$ mkvirtualenv -p python3 venv``

2. Ejecutar el ambiente. Podrían usar una librería que ya usen para crearlo de manera diferente.

``$ source venv/bin/activate``

3. Instalar las librerías.

``$ pip install -r requirements.txt``

4. Realizar migraciones y ejecutarlas

``$ python manage.py makemigrations``
``$ python manage.py migrate``

5. Activar el servidor

``$ python manage.py runserver``


Recursos API creados
--------------------

**Recurso para poblar la base de datos** (Ejecutar una sola vez)

**POST** ``http://localhost:8000/movie/populate``


Los recursos **GET**, tienen por defecto un sistema de estandarizado por HTTP de Rangos que carga datos por partes. Para el uso de paginación, se debe enviar la cabecera en el siguiente formato: **Range: 0-9** Donde el 0, se entiende como el **skip** interno de la base de datos y el 9 como el **limit**.


**Recurso para consultar películas relacionadas a un actor**

**GET** ``http://localhost:8000/movie/actor?actor=Jordan Ashwood``


**Recurso para consultar películas en orden por año**

**GET** ``http://localhost:8000/movie/year?sort=top_to_down``


**Recurso para consultar películas en orden por duración**

**GET** ``http://localhost:8000/movie/duration?sort=top_to_down``