## Instructions for running 
1. Open your terminal and navigate to the directory you wish to store the project and run the following command: 
```git clone https://github.com/margo-dubovik/CXDojoTestTask.git```
2. Create and activate venv
3. ```pip install -r requirements.txt```
4. Create a PostgreSQL database.
5. In the root of the project, create a file .env
In that file define the following variables:
```DJANGO_SECRET_KEY```,  ```DB_NAME```, ```DB_USER```, ```DB_PASSWORD```.
6. In terminal: ```python manage.py migrate```
7. ```python manage.py createsuperuser```, create a superuser.
8. ```python manage.py runserver```
You will be taken to login page. Log in with superuser credentials you`ve created on step 5.
9. Click the 'Collect information' button. 
10. Upload .csv and .xml files, press 'Collect Info'.
11. You`ll be redirected to the page with users info.