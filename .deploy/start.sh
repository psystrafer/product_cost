#!/bin/bash


### apply migrations
alembic upgrade head


### start consumer

fastapi run --port 8000 src/main.py