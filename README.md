# Sample app with FastAPI & Celery

Sample app, built to create an infrastructure envolving FastAPI and Celery

> App built using [Test Driven article](https://testdriven.io/courses/fastapi-celery/intro/) as a reference


## Celery

- Very powerful Task Message Management to work with async tasks in background, etc

### Commands

- Init Celery worker: `celery -A main.celery worker --loglevel=info`
- Use flower to monitor Celery tasks: `celery -A main.celery flower --port=5555`


## Alembic

- Database migration management for SQLAlchemy

### Commands

- Init Alembic: `alembic init alembic`
- Migrate database: `alembic revision --autogenerate`
- Updates the state of database based on application of all migrations: `alembic stamp head`
- Updates new migrations: `alembic upgrade head`
