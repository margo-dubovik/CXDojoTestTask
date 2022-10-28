## Instructions for running 
1. Open your terminal and navigate to the directory you wish to store the project and run the following command: 
```git clone https://github.com/margo-dubovik/CXDojoTestTask.git```
2. Open project in your code editor
3. Create and activate venv
4. ```pip install -r requirements.txt```
5. Create a PostgreSQL database.
6. In the root of the project, create a file .env
In that file define the following variables:
```DJANGO_SECRET_KEY```,  ```DB_NAME```, ```DB_USER```, ```DB_PASSWORD```.
7. In terminal:

```python manage.py makemigrations users```

```python manage.py migrate users```

```python manage.py migrate```


8. ```python manage.py createsuperuser```, create a superuser.
9. ```python manage.py runserver```
You will be taken to login page. Log in with superuser credentials you`ve created on previous step.
10. Click the 'Collect information' button. 
11. Upload .csv and .xml files, press 'Collect Info'.
12. You`ll be redirected to the page with users info.