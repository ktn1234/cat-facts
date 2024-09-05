# Cat Facts

Generate and get random cat facts using this web application using Django, Django Q, Boostrap5, HTMX, Crispy Forms, and Crispy Bootstrap5

## Create Project

django-admin startproject catfacts
python manage.py startapp catfactsapp

## Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

## Install Dependencies

pip install django
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install django-q

## Run Migrations

python manage.py makemigrations
python manage.py migrate

## Create Admin Account

python manage.py createsuperuser

## Run Server

python manage.py runserver
python manage.py qcluster

## Database Access

python manage.py dbshell
