# Flask API - Sistema de Autenticación, Roles y Permisos
Este proyecto es una API RESTful desarrollada en **Flask**, que incluye:
- Registro e inicio de sesión con JWT
- Roles y permisos vinculados a usuarios
- Protección de rutas con autorización basada en permisos
- Base de datos MongoDB Atlas usando MongoEngine
- Preguntas secretas en el registro


## Tecnologías y Librerías Usadas
FFlask==2.2.5
flask-cors==6.0.0
Flask-JWT-Extended==4.7.1
Flask-MongoEngine==1.0.0
Werkzeug==2.2.3
python-dotenv==1.1.0


## Estructura del Proyecto
```
app/
├── __init__.py
├── models/
│   ├── user.py
│   ├── role.py
│   └── permission.py
├── routes/
│   ├── auth.py
│   ├── role.py
│   ├── permission.py
│   └── product.py
├── middleware/
│   └── auth_middleware.py
├── config.py
main.py
.env
requirements.txt
README.md
```

## Instalación (Usando la terminal)
### 1. Clonar el repositorio
git clone https://github.com/tu_usuario/tu_proyecto.git
cd carpeta-donde-guardo-proyecto/ev_01

### 2. Crear entorno virtual
python3 -m venv venv
#En Linux/IoS: source venv/bin/activate  #En Windows: venv\Scripts\activate

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Crear archivo `.env`
MONGODB_URI=mongodb+srv://<usuario>:<password>@cluster.mongodb.net/db?retryWrites=true&w=majority
JWT_SECRET_KEY=tu_clave_super_secreta


## Ejecutar el servidor
python main.py
El servidor estará disponible en: `http://localhost:5000`


## Rutas disponibles
### Auth
| Método | Ruta                | Descripción                   |
|--------|---------------------|-------------------------------|
| GET    | `/secret-questions` | Obtener preguntas secretas    |
| POST   | `/register`         | Registro de usuario           |
| POST   | `/login`            | Login y generación de JWT     |

### Roles (token requerido)
| Método | Ruta          | Descripción              |
|--------|---------------|--------------------------|
| GET    | `/roles`      | Listar roles             |
| POST   | `/roles`      | Crear nuevo rol          |
| PUT    | `/roles/<id>` | Editar rol               |
| DELETE | `/roles/<id>` | Eliminar rol             |

### Permisos (token requerido)
| Método | Ruta               | Descripción              |
|--------|--------------------|--------------------------|
| GET    | `/permissions`     | Listar permisos          |
| POST   | `/permissions`     | Crear nuevo permiso      |
| PUT    | `/permissions/<id>`| Editar permiso           |
| DELETE | `/permissions/<id>`| Eliminar permiso         |

## 🔐 Seguridad

- JWT con duración de 5 minutos.
- Todas las rutas (excepto `/register` y `/login`) requieren token JWT.
- Los roles determinan los permisos del usuario.
- Se puede proteger rutas por permisos usando un decorador `@require_permission`.

## ✍️ Ejemplo de token

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

Usar en encabezado de las peticiones protegidas:

```
Authorization: Bearer <access_token>
```