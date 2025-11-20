async def test_calc(client, session):
    body = {
        "materials": [
            {"name": "steel", "qty": 120, "price": 54.5},
            {"name": "copper", "qty": 12.3, "price": 640.0}
        ]
    }

    response = await client.post("/calc", json=body)

    assert response.status_code == 201
    result = response.json()
    assert result == {"total_cost_rub": '14412.00'}
