# Nuclear sites REST API
REST API to realize CRUD operations on nuclear sites

## Overview
This project allow user to run a REST API to realize CRUD operations on nuclear sites. It uses Django REST Framework and its extension django-rest-framework-gis to manipulate geographic data. It uses PostgreSQL with PostGIS extension to store the data. 

## Getting started
This section is in development. It will further contain the instructions for deployed API usage.

## Steps to run the REST API locally

#### Requirements

Ensure you have the following software installed on your machine:

* Python (3.x recommended)
* PostgreSQL
* PostGIS (Spatial database extension for PostgreSQL)

#### Set PostgreSQL database and user

Create a PostgreSQL database with PostGIS extension : 

```
sudo apt install postgresql postgis 
```

Interact with the postgres database management system by typing :

```
potgres=# CREATE DATABASE nuclearsitesdb;
```

Add a database user and a password : 

```
postgres=# CREATE USER nuclearsitesapiuser WITH PASSWORD 'nuclearsitespassword';
```

Note the database name and user credentials must correspond to `DATABASES` section in `settings.py`.

Create PostGIS extension : 

```
$potgres=# CREATE EXTENSION postgis;
```

Specify encoding, default transaction isolation and timezone ith the following commands :

```
potgres=# ALTER ROLE nuclearsitesapiuser SET client_encoding TO 'utf8';
```

```
potgres=# ALTER ROLE nuclearsitesapiuser SET default_transaction_isolation TO 'read committed';
```

```
potgres=# ALTER ROLE nuclearsitesapiuser SET timezone TO 'UTC';
```

Specify user role as superuser :

```
postgres=# ALTER ROLE nuclearsitesapiuser SUPERUSER;
```

Give user full privileges to administer the database :

```
postgres=# GRANT ALL PRIVILEGES ON DATABASE nuclearsitesdb TO nuclearsitesapiuser;
```

#### Setup code

Create virtual environment for Python dependancies and activate it:

```bash
python3 -m venv nuclearsitesapi_venv
source nuclearsitesapi_venv/bin/activate
```

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

Once the project is running on your machine, you can perform CRUD operations with HTTP requests or directly using the web interface.

#### Admin Interface
This section is in development

## API Endpoints

* `/api/nuclear-sites/`:
    * GET: Retrieve a list of all nuclear sites stored in the database.
* `/apinuclear-sites/add/`:
    * POST : Create a new nuclear site element.
* `/api/nuclear-sites/{id}/`:
    * GET: Retrieve details of a specific nuclear site.
    * PUT: Update details of a specific nuclear site.
    * DELETE: Delete a specific nuclear site.

<!-- ## Tests

You can run the tests for this project with the following command :

```bash
python manage.py test
```
 -->


## License

This project is licensed under the Apach 2.0 License.