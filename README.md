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
