#!/bin/bash

alembic revision --autogenerate -m "БЛЯТЬ ЗАЕБАЛ"

alembic upgrade head

gunicorn app.src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000