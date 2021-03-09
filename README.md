# silverlog
Venv:
1.	Install virtual environment

2. 	Create virtual environment
	```virtualenv django_venv```

DON'T USE	python3 -m venv django_venv. Might be problems with installing packages.

3.	Activate virtual environment
	```source django_venv/bin/activate```

4.	To check what packages are installed into venv:
	```pip list``` or ```pip freeze```
-------------------------------	

1.	Install Django to venv:
	```pip3 install Django```

2.	Create Django project
	```django-admin startproject silverlog```

--------------------------------
Django & PostgreSQL
1.	Download postgres.
2.	Install psycopg2
	```pip3 install psycopg2```
	
3.	Setup postgres new db and user
```
	CREATE DATABASE silverlog;
	CREATE USER silverlog_admin WITH PASSWORD 'admin';
	ALTER ROLE silverlog_admin SET client_encoding TO 'utf8';
	ALTER ROLE silverlog_admin SET default_transaction_isolation TO 'read committed';
	ALTER ROLE silverlog_admin SET timezone TO 'UTC';
	GRANT ALL PRIVILEGES ON DATABASE silverlog TO silverlog_admin;
  ```
4.	Edit postgres configuration in settings.py file.
5.	Make migrations
	```python3 manage.py makemigrations``` and ```python3 manage.py migrate```
5.	Create superuser
	```python3 manage.py createsuperuser```
6.	Try to run server ```python3 manage.py runserver```
--------------------------------
Additional info:

* You can create new app ```python3 manage.py startapp appname```
* Requirements ```pip3 install django-crispy-forms```
