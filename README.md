# Incident API (FastAPI + SQLAlchemy + Alembic + Pydantic + Docker + Pytest)

Минимальный CRUD-сервис управления инцидентами. 

Методы API:
Инциденты (Incidents):
GET /incidents/ — список всех инцидентов
POST /incidents/ — создать новый инцидент
PATCH /incidents/{id} — обновить статус инцидента


## Быстрый старт (Docker Compose)
```bash
docker compose up -d
docker compose exec incident_api alembic revision --autogenerate -m "init" 
docker compose exec incident_api alembic upgrade head
```
http://localhost:8000/docs

## Запуск тестов 
```bash
docker compose exec incident_api pytest -v -s   
```

## Adminer (управление базой данных)
http://localhost:8080 
(данные для подключения в env файле)

## Alembic (миграция базы данных)
```bash
docker compose exec incident_api alembic revision --autogenerate -m "(название)"
docker compose exec incident_api alembic upgrade head  
```
