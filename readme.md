# USERS

## Overview

This project is a Flask-based web application for managing users and other resources. It connects to a MongoDB database and exposes APIs for user management and other functionalities. The app is containerized using Docker, making it easy to deploy across different environments.

## Features

- **User Management:** Create, read, update, and delete users.
- **Database Integration:** Uses MongoDB for persistent data storage.
- **Error Handling:** Centralized error handling for all routes.
- **Logging:** Application-level logging for debugging and monitoring.
- **CORS:** Cross-Origin Resource Sharing (CORS) enabled for API access from different domains.

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB
- **Containerization:** Docker
- **Authentication:** JWT (JSON Web Tokens)
- **Password Hashing:** bcrypt
- **Environment Management:** dotenv

## Requirements

- Python 3.9+
- MongoDB running locally or in the cloud (Mongo URI stored in `.env` file)
- Docker (for containerization)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/Vaibhav-crux/users_assignment.git
cd users_assignment
```

### 2. Create a `.env` file:

Create a `.env` file in the root directory with the following content:

```dotenv
MONGO_URI=mongodb://localhost:27017/yourdb
```

Replace `MONGO_URI` with your actual MongoDB URI and `SECRET_KEY` with a secure secret key for session management.

### 3. Install Python dependencies:

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Running the Application:

To run the application locally:

```bash
python main.py
```

The application will be available at `http://localhost:5000`.

### 5. Running the Application in Docker:

To run the application inside a Docker container:

1. **Build the Docker Image:**

```bash
docker build -t my-flask-app .
```

2. **Run the Docker Container:**

```bash
docker run -p 5000:5000 my-flask-app
```

This will start the Flask app in the Docker container, and you can access it on `http://localhost:5000`.

### 5. API Endpoints

- **GET /api/users:** Fetch all users
- **GET /api/users/{id}:** Fetch user by ID
- **POST /api/users:** Create a new user
- **PUT /api/users/{id}:** Update an existing user
- **DELETE /api/users/{id}:** Delete a user
