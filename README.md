## Instructions for running 
1. open your terminal and navigate to the directory you wish to store the project and run the following command: 
```git clone https://github.com/margo-dubovik/CXDojoTestTask.git```
2. create and activate venv
3. ```pip install -r requirements.txt```
4. ```python manage.py migrate```
5. ```python manage.py createsuperuser```, create a superuser.
6. ```python manage.py runserver```
You will be taken to login page. Log in with superuser credentials you`ve created on step 5.
7. Click the 'Collect information' button. 
8. Upload .csv and .xml files, press 'Collect Info'.
9. You`ll be redirected to the page with users info.