# Snippet Manager

A simple Django application for managing code snippets. Users can create, view, edit, and delete their snippets. The application requires user authentication to ensure that snippets are private to each user.

## Features

- User authentication (login/logout)
- Create new snippets
- View a list of snippets
- View details of a specific snippet
- Edit existing snippets
- Delete snippets

## Technologies Used

- Django
- Python
- HTML/CSS
- Postgresql

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the repository:**

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Register/Login**: Users can register and log in to access their snippets.
- **Create Snippet**: After logging in, users can create new snippets using the provided form.
- **View Snippets**: Users can view a list of their snippets and click on any snippet to see its details.
- **Edit/Delete Snippets**: Users can edit or delete their snippets as needed.