# Nuclear sites REST API
REST API to realize CRUD operations on nuclear sites

## Overview
This project aims to create a REST API to realize CRUD operations on nuclear sites. It uses Django REST Framework and its extension django-rest-framework-gis to manipulate geographic data.

## Installation

#### Requirements

Ensure you have the following software installed on your machine:

* Python (3.x recommended)
* Django (3.x recommended)
* PostgreSQL (with PostGIS extension)
* PostGIS (Spatial database extension for PostgreSQL)
* Git

#### Setup

Clone the repository:

```bash
git clone https://github.com/barney11/nuclear-rest-api.git
```

Navigate to the project directory:


```bash
cd nuclear-rest-api
```

Install dependencies:

```bash
pip install .
```

Create and apply database migrations:

```bash
python manage.py migrate
```

Create a superuser for admin access:


```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Your project should now be running at http://localhost:8000/. You can access the admin interface at http://localhost:8000/admin/.

## Usage

Provide detailed instructions on how to use your Django REST Framework GIS API. Include information on how to interact with the API endpoints, make requests, and any additional configuration.

#### Admin Interface

* Access the admin interface at http://localhost:8000/admin/.
* Log in with the superuser credentials created during the setup.
* Manage nuclear sites and other relevant data using the Django admin interface.

## API Endpoints

List and describe the available API endpoints along with the methods they support (e.g., GET, POST, PUT, DELETE).

* /api/nuclear-sites/: [Description]
    * GET: Retrieve a list of all nuclear sites.
    * POST: Create a new nuclear site.
* /api/nuclear-sites/{id}/: [Description]
    * GET: Retrieve details of a specific nuclear site.
    * PUT: Update details of a specific nuclear site.
    * DELETE: Delete a specific nuclear site.

Include any additional information that users might need to know about your API.

## Tests

You can run the tests for this project with the following command :

```bash
python manage.py test
```

## License

This project is licensed under the Apach 2.0 License.