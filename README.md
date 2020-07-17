# Ubiwhere-Challenge

Basic Django REST API to manage urban occurrences for the Ubiwhere challenge.

## Instalation Guide
Note: This installation guide is made for Ubuntu based linux only.
 1. Install Python3.7 in your machine
 
 2. Create a virtual environment for this project and enter it
 python3.7 -m pip install virtualenv
 python3.7 -m virtualenv venv
 source venv/bin/activate
 
 3. Install python modules in requirements.txt
 python3.7 -m pip install -r requirements.txt
 
 4. Install  [PostgreSQL](https://postgresql.org) database with [PostGIS](https://postgis.net/) ( a spatial database extender for PostgreSQL)
 wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt install postgresql-10
sudo apt install postgresql-10-postgis-2.4
sudo apt install postgresql-10-postgis-scripts
sudo apt install postgis

5. Create project database and database superuser
- sudo -u postgres -i - enters sudo shell with postgres users
- psql - enters postgres console
- CREATE DATABASE mydatabase; - creates project database
- CREATE USER testuser WITH PASSWORD 'password1' - Creates database user for the project
- ALTER ROLE testuser SUPERUSER - Sets testuser as database superusers (needed for PostGIS)
- Exit postgress console and sudo shell

6. Apply migrations to the new database
python manage.py migrate

7. Create Django project superuser
python manage.py createsuperuser


## API Endpoints
The endpoints are implemented using Django Rest Framework [DefaultRouter](https://www.django-rest-framework.org/api-guide/routers/#defaultrouter) class.

### Endpoints List
[WIP]

Few things to note:

 - Category endpoints require staff authentication
 - Occurrence endpoints allow PUT and PATCH requests only when the user making the request is the owner of the occurrence, or is staff.
 - Only staff can update occurrence status. 

### Postman Collection
To easily present and test the implemented endpoints a Postman Collection is provided [here](https://www.getpostman.com/collections/af5ca37b2c5550c8ad86)
