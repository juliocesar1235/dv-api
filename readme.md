# Dvapi

Api to manage MX zipcodes

## Description

This a Django rest api running mysql for db engine, making available CRUD operations to a vast MX zipcodes repertoire

**Only zipcodes available for Nuevo Leon and Baja California due to db restriction cost"

## Problem

I thought about a couple of problems from the start,

* Setting up the local environment to work with mysql since its not my primary db option to work on

* How are we going to insert that much data from the excel file to the database

* Deployment setup in the cloud or instance, must of the times the deployment part is very tricky due to configuration errors in the server

## Solutions

* Setting up the local env with django documentation and configuring manually the database with a specific user for the app

* For the massive data insertion there where multiple options, I chose to create a post endpoint and develop a script that processed the data and send it to the api. I chose this option due to security risks with a csv import or a db_dump directly to the database. Also sending the file in base64 was not an option since it will be very heavy to send in the request since some of them have por than 5000 rows

* For deployment I chose to use a digital ocean droplet with restricted specs(low tier billing). Its using nginx and gunicorn to serve the requests to the api.

## Architecture

The api is structured very simple and follows the django framework rules by using the different layer provided such as:

* models
* serializers
* services
* views
* urls

## Getting Started

### Dependencies

* python3
* mysql
* pip or pip3
* venv

### Executing program

* Step-by-step bullets
```
python manage.py runserver
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Julio Gutierrez 
[Linkedin](https://www.linkedin.com/in/julio-gutierrez1235/)

## Version History

* 1.0

## License

This project is licensed under the [Julio Gutierrez] License - see the LICENSE.md file for details
