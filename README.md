
# Ubiwhere-Challenge

Basic Django REST API to manage urban occurrences for the Ubiwhere challenge.

## Instalation Guide
To note that this installation guide is made for Ubuntu based linux only.

### MANUAL Instalation Guide
 1. Clone the repository

 2. Install Python3.7 in your machine
 
 3. Create a virtual environment for this project and enter it
 	- ```python3.7 -m pip install virtualenv```
 	- ```python3.7 -m virtualenv venv```
 	- ```source venv/bin/activate```
 
 4. Install python modules in requirements.txt
	- ```python3.7 -m pip install -r requirements.txt```
 
 5. Install  [PostgreSQL](https://postgresql.org) database with [PostGIS](https://postgis.net/) ( a spatial database extender for PostgreSQL)
	- ```wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -```
	- ```sudo apt update```
	- ```sudo apt install postgresql-10```
	- ```sudo apt install postgresql-10-postgis-2.4```
	- ```sudo apt install postgresql-10-postgis-scripts```
	- ```sudo apt install postgis```

6. Create project database and database superuser
	- ```sudo -u postgres -i``` - enters sudo shell with postgres users
	- ```psql``` - enters postgres console
	- ```CREATE DATABASE mydatabase;``` - creates project database
	- ```CREATE USER testuser WITH PASSWORD 'password1'``` - Creates database user for the project
	- ```ALTER ROLE testuser SUPERUSER``` - Sets testuser as database superusers (needed for PostGIS)
	- Exit postgress console and sudo shell

7. Apply migrations to the new database
	- ```python manage.py migrate```

8. Create Django project superuser
	- ```python manage.py createsuperuser```

9. Populate the category model with the initial entries
	- ```python manage.py loaddata categories-fixture.json```  

10. Run _Django_ server
	- ```python manage.py runserver 0.0.0.0:8000```


### DOCKER Instalation Guide
Alternatively, this project can be installed via Docker. It is assumed that docker and docker-compose are already installed. You can do so by following this guide for [docker installation](https://docs.docker.com/engine/install/ubuntu/) and for [docker-compose installation](https://docs.docker.com/compose/install/)

Note: in order to run the project via docker please change the database configuration in _ubiwhere/settings.py_ from ```'HOST': '127.0.0.1'``` to ```'HOST': 'db'```. 
1. Clone the repository 

2. Build docker-compose 
	- ```sudo docker-compose build```

3. Apply migrations to the database
	- ```sudo docker-compose run web python3 manage.py migrate```

4. Create project superuser
	- ```sudo docker-compose run web python3 manage.py createsuperuser``` 

5. Populate the category model with the initial entries
	- ```sudo docker-compose run web python3 manage.py loaddata categories-fixture.json```  

6. Run docker containers
	- ```sudo docker-compse up``` 


## API Endpoints
The endpoints are implemented using Django Rest Framework [DefaultRouter](https://www.django-rest-framework.org/api-guide/routers/#defaultrouter) class.

### Endpoints List

|Route| GET | POST |  DELETE |  PATCH/PUT |
|--|--|--|--|--|
|/occurrences/| list all occurrences | add occurrence |------------------ | ------------------ | 
|/occurrences/{pk}/| retrieve occurrence _pk_ | ------------------ | delete occurrence _pk_ | update occurrence _pk_  |
|/categories/| list all categories| add category | ------------------ | ------------------ |
|/categories/{pk}/| retrieve category _pk_ | ------------------  | delete category _pk_ | update category _pk_ |

Few things to note:
 - Category endpoints require staff authentication.
 - Occurrence endpoints allow PUT and PATCH requests only when the user making the request is the owner of the occurrence, or is staff.
 - Only staff can update occurrence status. 
 - Users need to be authenticated to add, modify and delete an occurrence entry.
 - User management is made via the Django admin dashboard.

### Postman Collection
To easily present and test the implemented endpoints a Postman Collection is provided [here](https://www.getpostman.com/collections/af5ca37b2c5550c8ad86)
