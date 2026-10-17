# 👺 Demon Slayer RESTful API

![Demon Slayer Logo](media/Demon-Slayer-Logo.png)

A lightweight and simple RESTful API built with **Django REST framework** (Python) to access data about slayer characters, breathing styles, and roles from the *Kimetsu No Yaiba* universe.


## 🛠️ Tech Stack

---
| Component | Technology | Purpose |
| :--- | :---| :--- |
| **Backend** | [![Backend](https://skillicons.dev/icons?i=py,django)](https://github.com/DaniDevGS/Demon-Slayer-API)| RESTful server and data logic. |
| **Database** | [![Database](https://skillicons.dev/icons?i=sqlite)](https://github.com/DaniDevGS/Demon-Slayer-API) | API data storage. |
| **Frontend** | [![Frontend](https://skillicons.dev/icons?i=html,css)](https://github.com/DaniDevGS/Demon-Slayer-API) | Welcome page and API documentation. |
---



## 🚀 Setup and Installation

Follow these steps to run the API in your local environment.

### Prerequisites

- **Python 3+**
- **`pip`** (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/DaniDevGS/Demon-Slayer-API-REST
cd Demon-Slayer-API-REST
```

### 2. Create Virtual Environment and Install Dependencies

Using a virtual environment is recommended to isolate project dependencies.

```bash
# Create virtual environment 
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies 
pip install -r requirements.txt
```

### 3. Environment Variables Configuration
In the `.env_example` file, it looks like this:

```bash
SECRET_KEY=your_secret_key
DEBUG=your_debug
```

### 4. Run the Application

Run the Django server:
```bash
python manage.py runserver 0.0.0.0:8000
```

## 📚 API Endpoints

The API exposes the following REST endpoints (currently supports GET requests only):

### Slayers
---
| Method | Endpoint | Description |
| :--- | :---| :--- |
| **GET** | **/api/cazadores/** | Retrieves the full list of all demon slayers. |
| **GET** | **/api/cazadores/id/** | Retrieves a specific slayer by ID. |
---

#### Example: Retrieve a Character
To retrieve information for Tanjiro Kamado (ID 1), send a request to:
```bash
GET http://localhost:8000/api/cazadores/1
```

##### Response (JSON):
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

### Breathing Styles
---
| Method | Endpoint | Description |
| :--- | :---| :--- |
| **GET** | **/api/respiraciones/** | Retrieves the full list of all Demon Slayer breathing styles. |
| **GET** | **/api/respiraciones/id/** | Retrieves a specific breathing style by ID. |
---

### Forms
---
| Method | Endpoint | Description |
| :--- | :---| :--- |
| **GET** | **/api/posturas/** | Retrieves the full list of all Demon Slayer breathing forms. |
| **GET** | **/api/posturas/id/** | Retrieves a specific breathing form by ID. |
---

### Roles
---
| Method | Endpoint | Description |
| :--- | :---| :--- |
| **GET** | **/api/roles/** | Retrieves the full list of all narrative roles in Demon Slayer. |
| **GET** | **/api/roles/id/** | Retrieves a specific narrative role by ID. |
---
