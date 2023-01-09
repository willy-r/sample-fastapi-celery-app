# Sample app with FastAPI & Celery

Sample app, built to create an infrastructure envolving FastAPI and Celery

> App built using [Test Driven article](https://testdriven.io/courses/fastapi-celery/intro/) as a reference


## Running locally

1. Changes `.env.example` to `.env`
2. Run and develop with **docker-compose**: docker compose up -d --built
3. Access [http://localhost:5557](http://localhost:5557) to see the server and [http://localhost:8010](http://localhost:8010) to access flower 


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
