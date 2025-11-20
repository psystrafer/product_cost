# Проект расчета цен

## Запуск из папки проекта
```docker compose up -d```

## Пример curl
```
curl -X 'POST' \
  'http://localhost:8000/calc' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"materials": [
{"name": "steel", "qty": 120, "price": 54.5},
{"name": "copper", "qty": 12.3, "price": 640.0}
]
}'
```

## SQL запрос 10 последних 
```
SELECT *
FROM calc_result cr 
ORDER BY created_at  DESC
LIMIT 10;
```

## Запуск тестов
### 1. Создайте локальное окружение:
```python3 -m venv product-cost``` для примера.

### 2. Установить зависимости 
```pip install poetry```
```poetry install```

### 3. Поднять pg:
```docker run --name test-pg -p 5432:5432 -e POSTGRES_USER=test_user -e POSTGRES_PASSWORD=test_password -e POSTGRES_DB=meta_test_db -d postgres```

### 4. Запуск тестов: 
```PC_ENV=.test.env pytest```
