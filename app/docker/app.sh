#!/bin/bash

# Ожидание старта базы данных
until pg_isready -h db_app -p 5432 -U "$POSTGRES_USER"; do
  echo "Waiting for postgres container..."
  sleep 2
done

echo "Postgres is ready. Running migrations..."

# Запуск миграций Alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# Запуск приложения
exec gunicorn app.src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
