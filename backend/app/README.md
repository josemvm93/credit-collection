# API

## Steps to run

- Have [python](https://www.python.org/) installed
  
```python
        python --version
```
- Install pipenv, this tool makes the best of the package worlds (bundler, composer, npm, etc.) available to Python developers.To install pipenv, just open terminal and type the following command.

```python
        pip install pipenv
```

- Python and pipenv together are enough to start developing our Flask applications, we need to configure a database engine. In this case,  going to use [SQLAlchemy](https://www.sqlalchemy.org/)to save and bring data from the engine that we have chosen.

- Install [Podman](https://podman.io/) or other conteiner software like [Docker] (https://www.docker.com/)
```
        podman pod create --name postgresql -p 5432 -p 9187

        podman run -d --pod postgresql -e POSTGRES_PASSWORD=password postgres:latest

```

-  Init virtual environment with

```
        pipenv --three

        pipenv shell

        pipenv run
```
- Finally
  - Initialize the database 
  ```
        python manage.py seed_db
  ```

    Type "Y" to accept the message (which is just there to prevent you accidentally deleting things -- it's just a local Postgres database). Also has a basic users to access the frontend.
    - Run app with:
        ```
            python main.py
        ```   