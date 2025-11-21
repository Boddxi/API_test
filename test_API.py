import requests

#Тест-кейс 1: Создание избранного места с корректно заполненными обязательными полями
def test_case_1():
    body = {
        "title": "Тестовое место",
        "lat": 41.89193,
        "lon": 12.51133
    }
    headers = {'Content-Type': 'application/json', 'Cookie': 'f3a7d0ba35e94caeabf22554dfdb2e3e'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f"Ожидался статус 200, но получили {response.status_code}"

    response_data = response.json()
    required_fields = ['id', 'title', 'lat', 'lon', 'color', 'created_at']

    for field in required_fields:
        assert field in response_data, f"Отсутствует поле: {field}"

    assert response_data['title'] == body['title']
    assert response_data['lat'] == body['lat']
    assert response_data['lon'] == body['lon']
    assert response_data['color'] is None
    assert response_data['id'] > 0

    created_at = response_data['created_at']
    parts = created_at.split(' ')

    assert len(parts) == 2, f"Неверный формат даты"

    date_parts = parts[0].split('-')
    time_parts = parts[1].split(':')

    assert all(part.isdigit() for part in date_parts), f"Дата должна содержать только цифры: {parts[0]}"
    assert all(part.isdigit() for part in time_parts), f"Время должно содержать только цифры: {parts[1]}"

    #Тест-кейс 2: Создание избранного места с указанием всех допустимых цветов (по очереди)



