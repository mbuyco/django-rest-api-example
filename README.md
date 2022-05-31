# Django Rest API Sample Code

## Installation

```
python -m venv venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## Docker

```
docker-compose up -d --build
docker-compose exec web sh
    > pip install -r requirements.txt
    > python manage.py makemigrations
    > python manage.py migrate
    > python manage.py runserver
```
