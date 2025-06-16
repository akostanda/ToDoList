# ToDoList
A small Django project for managing tasks.


## Technologies
- Python 3.12
- Django 5.2.3
- PostgreSQL


# Project settings
1. Clone this project's repository to your local machine using SSH
    ```bash
      git git@github.com:akostanda/ToDoList.git
    ```
2. Move to it
    ```bash
      cd ToDoList
           or
      cd <your project name>
    ```
3. Create and activate a virtual environment
    ```bash
      python3 -m venv venv
      source venv/bin/activate
    ```
4. Install the necessary dependencies
    ```bash
      pip install -r requirements.txt
    ```
5. Set up the database
   - Install PostgreSQL
     ```bash
       sudo apt update
       sudo apt install postgresql postgresql-contrib
     ```
   - Log in to the PostgreSQL console as the postgres user
     ```bash
       sudo -u postgres psql
     ```
   - Create a database
     ```bash
       CREATE DATABASE to_do_list;
     ```
   - Create a user with a password
     ```bash
       CREATE USER my_user WITH PASSWORD 'my_password';
     ```
   - Make the user the owner of the database
     ```bash
       ALTER DATABASE to_do_list OWNER TO my_user;
     ```
   - Grant the user the privilege to create new databases
     ```bash
       ALTER ROLE my_user CREATEDB;
     ```
   - Exit the PostgreSQL console
     ```bash
       \q
     ```
#### NB: Please feel free to change the database name, user name and password. If you want to use your own ones, you should export them as environment variables:
    ```bash
      export POSTGRES_DB=<your database name>
      export POSTGRES_USER=<your user name>
      export POSTGRES_PASSWORD=<your password>
      export POSTGRES_HOST=<your host>
      export POSTGRES_PORT=<your port>
    ```
6. Apply migrations before first run
    ```bash
      python3 manage.py migrate
    ```
7. Create a superuser (required to log in)
    ```bash
      python3 manage.py createsuperuser
    ```
NB: You should set name, email and password for the superuser, which will be used to log in to the admin panel.
8. Run the server
    ```bash
      python3 manage.py runserver
    ```
9. Run the tests
    ```bash
      python3 manage.py test
    ```

## Addition information
- The website will be available at: http://127.0.0.1:8000
- The admin panel will be available at: http://127.0.0.1:8000/admin
- Django admin login: http://127.0.0.1:8000/admin/
- The API documentation is stored in [API_Documentation.yaml](API_Documentation.yaml)
- The Swagger UI will be available at: http://127.0.0.1:8000/swagger/
