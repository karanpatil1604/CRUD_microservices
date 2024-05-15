# Running the app on local machine

> To run django server follow this

## Make sure you have postgres server installed and running on your local machine

`set the environment variables for postgres database`

### If not set these defaults will be used

```
'NAME': os.getenv('DB_NAME', 'mydatabase'),
'USER': os.getenv('DB_USER', 'postgres'),
'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
'HOST': os.getenv('DB_HOST', 'localhost'),
'PORT': os.getenv('DB_PORT', '5432'),
```

## Finished setting postgres; Now create the tables

    (.env)django_app> python manage.py makemigrations
    (.env)django_app> python manage.py migrate

---

```
>cd django_app
>python -m venv .env
>.env/Scripts/activate
>pip install -r requirements.txt
```

> To run fastapi server follow this

```
>cd fastapp
>python -m venv .env
>.env/Scripts/activate
>pip install -r requirements.txt
```

> make sure servers are running for both the apps
```
- Django default port is not used

(.env)django_app> python manage.py runserver 8001
```

- fastapp runs on port 8000

```
(.env)fastapp> python app.py
```