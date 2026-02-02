# 👺 Demon Slayer RESTful API

![Demon Slayer Logo](media/Demon-Slayer-Logo.png)

Una API RESTful ligera y sencilla construida con **Django REST framework** (Python) para acceder a datos de cazadores, estilos de respiración y roles del universo de *Kimetsu No Yaiba*.


## 🛠️ Stack Tecnológico

---
| Componente | Tecnología | Propósito |
| :--- | :---| :--- |
| **Backend** | [![Backend](https://skillicons.dev/icons?i=py,django)](https://github.com/DaniDevGS/Demon-Slayer-API)| Servidor RESTful y lógica de datos. |
| **Base de Datos** | [![Data Base](https://skillicons.dev/icons?i=sqlite)](https://github.com/DaniDevGS/Demon-Slayer-API) | Almacenamiento de los datos de la API. |
| **Frontend** | [![Frontend](https://skillicons.dev/icons?i=html,css)](https://github.com/DaniDevGS/Demon-Slayer-API) | Página de bienvenida y documentación de la API. |
---



## 🚀 Instalación y Ejecución

Sigue estos pasos para levantar la API en tu entorno local.

### Prerequisitos

* **Python 3+**
* **`pip`** (Python package installer)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/DaniDevGS/Demon-Slayer-API-REST
cd Demon-Slayer-API-REST
```

### 2. Crear Entorno Virtual e Instalar Dependencias

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto.

```bash

# Crear entorno virtual 
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias 
pip install -r requirements.txt
```

### 3. Configuracion de variables de entorno
En el archivo .env_example aparece tal que asi

```bash
SECRET_KEY=tu_secret_key
DEBUG = tu_debug
```

### 4. Ejecutar la Aplicación

Ejecuta el servidor de Django:
```bash
python manage.py runserver 0.0.0.0:8000
```

## 📚 Endpoints de la API

La API expone los siguientes puntos de conexión REST (actualmente solo soporta GET):

### Cazadores
---
| Metodo | Endpoint | Descripción |
| :--- | :---| :--- |
| **GET** | **/api/cazadores/** | Obtiene la lista completa de todos los cazadores de demonios.	 |
| **GET** | **/api/cazadores/id/** | Obtiene un cazador específico por su id. |
---

#### Ejemplo: Obtener un Personaje
Para obtener la información de Tanjiro Kamado (ID 1), haz una solicitud a:
```bash
GET http://localhost:8000/api/cazadores/1
```

##### Respuesta (JSON):
```json
{
    "id": 1,
    "nombre": "Tanjiro Kamado",
    "descripcion": "Tanjirō Kamado es el protagonista de la serie de manga Kimetsu no Yaiba. Es un adolescente que emprende una búsqueda para restaurar la humanidad de su hermana, Nezuko, quien se convirtió en un demonio después de que su familia fuera asesinada por Muzan Kibutsuji.",
    "rol": "Principales",
    "imagen": "/media/imagenes/Tanjiro_Anime.webp",
    "respiracion": [
        "Respiración del Sol",
        "Respiración del Agua"
    ]
}
```

### Respiraciones
---
| Metodo | Endpoint | Descripción |
| :--- | :---| :--- |
| **GET** | **/api/respiraciones/** | Obtiene la lista completa de todas las respiraciones de Demon Slayer	 |
| **GET** | **/api/respiraciones/id/** | Obtiene una respiracion específica por su id. |
---

### Posturas
---
| Metodo | Endpoint | Descripción |
| :--- | :---| :--- |
| **GET** | **/api/posturas/** | Obtiene la lista completa de todas las posturas de las respiraciones de Demon Slayer	 |
| **GET** | **/api/posturas/id/** | Obtiene una posturas específica por su id. |
---

### Roles
---
| Metodo | Endpoint | Descripción |
| :--- | :---| :--- |
| **GET** | **/api/roles/** | Obtiene la lista completa de todos los roles narrativos de Demon Slayer.	 |
| **GET** | **/api/roles/id/** | Obtiene un rol narrativo específico por su id. |
---
