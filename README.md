# django-project-template

A project template for Django 2.0 based on the django-two-scoops project template.

## Usage

```
python3 -m venv .env
source .env/bin/activate
pip install django
django-admin.py startproject --template=https://github.com/tom-henderson/django-template/archive/master.zip --extension=py,rst,html project_name
pip install -r requirements/local.txt
npm install
python project_name/manage.py migrate
python project_name/manage.py collectstatic
python project_name/manage.py runserver
```
