### STUDENT RESOURCES HUB

Student Resources Hub - Campus Resources Sharing Platform

## OVERVIEW

Student Resources Hub is a Django-based backend project designed to create a centralized platform for sharing and accessing campus resources. 
Whether it's lecture notes, study materials, or event information, this platform aims to streamline resource sharing within the campus community.

### FEATURES

- **User Authentication**: Secure user registration and login functionality to ensure a personalized and protected experience.

- **Resource Upload and Download:** Users can easily upload and download various resources, allowing a collaborative learning environment

- **User Profiles**: Personalized user profiles that showcase uploaded resources and contributions.
  
- **Search Functionality**: Efficient search capabilities to quickly locate and access the desired resources.

## GETTING STARTED

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Aladaabdul/Student-Resources-Hub.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Student-Resources-Hub
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to [http://localhost:8000](http://localhost:8000) to view the application.

### Usage

1. Navigate to the [http://localhost:8000/admin](http://localhost:8000/admin) page and log in with your superuser account.

2. Use the Django admin interface to manage users, resources, and other aspects of the application.

3. Explore the resource sharing platform by logging in with a regular user account.

### Testing

Running Tests

1. Make sure you have installed all dependencies:
   ```bash
    pip install -r requirements.txt
    ```
2. Run the tests using the following command:
   ```bash
     pytest
   ```

Key test cases included in the project

Create Resource as Anonymous User: Tests that anonymous users cannot create new resources and return a 401 status.

Create Resource as Authorized User: Tests that authorized users can successfully create new resources and return a 201 status.

Delete Resources as Authorized and Anonymous Users: Tests for different outcomes based on user authentication.

Update Resources: Verifies that only authorized users can update existing resources.


### API Documentation

- **Swagger UI**: Explore the API endpoints using the Swagger UI.
  - Access Swagger UI: [http://localhost:8000/hubs/schema/swagger-ui/](http://localhost:8000/hubs/schema/swagger-ui/)
