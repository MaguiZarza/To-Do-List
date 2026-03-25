# Django Notes and To-Do App

Este proyecto es una aplicación web desarrollada con Django que incluye dos funcionalidades principales organizadas en diferentes apps:

* Gestión de notas
* Lista de tareas (To-Do List)

## Descripción

La aplicación permite al usuario crear, visualizar y eliminar notas, así como gestionar tareas en una lista independiente. Cada funcionalidad está separada en su propia app dentro del proyecto, siguiendo una estructura modular.

## Funcionalidades

### App de Notas (`notes`)

* Crear notas
* Ver listado de notas
* Ver detalle de cada nota
* Eliminar notas

### App de Tareas (`to_do`)

* Crear tareas
* Marcar tareas
* Visualizar lista de tareas
* Eliminar tareas

## Tecnologías utilizadas

* Python
* Django
* HTML
* CSS
* SQLite

## Estructura del proyecto

* `notes/`: app para gestión de notas
* `to_do/`: app para lista de tareas
* `templates/`: templates compartidos
* `to_do_project/`: configuración principal del proyecto
* `db.sqlite3`: base de datos
* `manage.py`: gestor de comandos de Django
* `requirements.txt`: dependencias del proyecto

## Ejecución del proyecto

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
```

2. Crear y activar entorno virtual:

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:

```bash
python manage.py migrate
```

5. Ejecutar el servidor:

```bash
python manage.py runserver
```

6. Acceder desde el navegador:

```
http://127.0.0.1:8000/
```

## Notas

El proyecto está organizado en múltiples apps para facilitar la escalabilidad y el mantenimiento del código.
Cada funcionalidad puede evolucionar de forma independiente.
