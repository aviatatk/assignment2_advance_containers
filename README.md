# WorkWise - Django Web Application

## Overview
WorkWise is a web application built using Django, designed to manage user authentication and role-based access. It provides a robust and scalable framework for handling users, permissions, and application workflows.

## Features
- User authentication (login/logout, password reset)
- Role-based access control
- API endpoints for user management
- Docker support for easy deployment
- Logging system for application monitoring

## Tech Stack
- **Backend**: Django (Python)
- **Database**: PostgreSQL (or SQLite for development)
- **Containerization**: Docker, Docker Compose
- **Web Server**: Nginx (Reverse Proxy)

## Installation Guide
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip
- virtualenv (optional but recommended)
- Docker & Docker Compose (if using containers)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd workwise_02/web
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   The application will be available at `http://127.0.0.1:8000/`.

## Running with Docker
1. **Build and Run Containers**:
   ```bash
   docker-compose up --build
   ```
2. The application should be accessible at `http://localhost/` (configured via Nginx).

## Logs
Logs are stored in the `logs/` directory. If using Docker, logs can be accessed using:
```bash
docker logs <container_id>
```

## API Documentation

### **Authentication Endpoints (JWT)**
These endpoints are provided by **`djangorestframework-simplejwt`** for token-based authentication.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/token/` | Obtain JWT access and refresh tokens. |
| `POST` | `/api/token/refresh/` | Refresh the access token using the refresh token. |

#### **Example Request (Token Generation)**
```bash
curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "securepassword"}'
```

### **User Endpoints**
These endpoints allow authenticated users to manage their profiles and passwords.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/user/profile/` | Retrieve the logged-in user’s profile. |
| `PUT` | `/api/user/profile/` | Update user profile (partial update allowed). |
| `POST` | `/api/user/change-password/` | Change the user’s password. |

#### **Example Request (Retrieve Profile)**
```bash
curl -X GET http://localhost:8000/api/user/profile/ \
     -H "Authorization: Bearer <ACCESS_TOKEN>"
```

#### **Example Request (Change Password)**
```bash
curl -X POST http://localhost:8000/api/user/change-password/ \
     -H "Authorization: Bearer <ACCESS_TOKEN>" \
     -H "Content-Type: application/json" \
     -d '{"old_password": "oldpass123", "new_password": "newpass123"}'
```

### **Admin Endpoints (Restricted Access)**
These endpoints are **only accessible to admin users**.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/admin/users/` | Retrieve a list of all users. |
| `GET` | `/api/admin/users/<id>/` | Retrieve a specific user’s details. |
| `POST` | `/api/admin/users/register/` | Register a new user (admin-only). |

#### **Example Request (Retrieve User List)**
```bash
curl -X GET http://localhost:8000/api/admin/users/ \
     -H "Authorization: Bearer <ADMIN_ACCESS_TOKEN>"
```

#### **Example Request (Register a New User)**
```bash
curl -X POST http://localhost:8000/api/admin/users/register/ \
     -H "Authorization: Bearer <ADMIN_ACCESS_TOKEN>" \
     -H "Content-Type: application/json" \
     -d '{
           "username": "newuser",
           "first_name": "John",
           "last_name": "Doe",
           "email": "john.doe@example.com",
           "password": "securepass",
           "password2": "securepass"
         }'
```

### **Security & Authentication**
- Uses **JWT (JSON Web Token)** for authentication.
- Admin access is required for managing users (`IsAuthenticated`, `IsAdminUser` permissions).
- Password validation is enforced using Django’s `validate_password`.



