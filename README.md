# ToDoApp

## Overview

Welcome to ToDoApp, a simple task management application built with Python and Django. This application leverages Docker for PostgreSQL, providing a hassle-free setup for database management.

## Features

- User authentication.
- Profile details editing for a personalized experience.
- Easy addition and deletion of tasks.

## Prerequisites

Make sure you have Docker and Python installed on your machine.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/M370D1/ToDoApp.git
   cd ToDoApp

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
 - Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
   
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Start the PostgreSQL database using Docker:
   ```bash
   docker run -d \
     --name todo-postgres \
     -e POSTGRES_USER=postgres-user \
     -e POSTGRES_PASSWORD=password \
     -e POSTGRES_DB=ToDo_DB_2 \
     -p 5432:5432 \
     postgres:latest

5. Apply database migrations and start the app:
   ```bash
   python manage.py migrate
   python manage.py runserver

  The app will be accessible at http://localhost:8000/.

## Usage

Access the app in your browser and register or log in.
Edit your profile details for a personalized touch.
Easily add and delete todos to manage your tasks efficiently.
