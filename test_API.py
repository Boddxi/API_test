import requests


def get_session_token():
    response = requests.post('https://regions-test.2gis.com/v1/auth/tokens')
    token = response.cookies.get('token')
    return token


# Тест-кейс 1: Создание избранного места с корректно заполненными обязательными полями
def test_case_1():
    token = get_session_token()

    data = {
        "title": "Тестовое место",
        "lat": 41.89193,
        "lon": 12.51133
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 200, f"Ожидался статус 200, но получили {response.status_code}"

    response_data = response.json()
    required_fields = ['id', 'title', 'lat', 'lon', 'color', 'created_at']

    for field in required_fields:
        assert field in response_data, f"Отсутствует поле: {field}"

    assert response_data['title'] == data['title']
    assert response_data['lat'] == data['lat']
    assert response_data['lon'] == data['lon']
    assert response_data['color'] is None
    assert response_data['id'] > 0

    created_at = response_data['created_at']

    assert 'T' in created_at, f"Неверный формат даты: {created_at}"
    assert ':' in created_at, f"Неверный формат времени: {created_at}"

    parts = created_at.split('T')

    assert len(parts) == 2, f"Неверный формат даты"

    date_part = parts[0]
    time_part = parts[1]

    date_parts = date_part.split('-')
    assert len(date_parts) == 3, f"Неверный формат даты: {date_part}"
    assert all(part.isdigit() for part in date_parts), f"Дата должна содержать только цифры: {date_part}"

    time_part, tz_part = time_part.split('+')
    time_part = time_part.split(':')
    tz_part = tz_part.split(':')
    assert len(time_part) == 3, f"Неверный формат времени: {time_part}"
    assert all(part.isdigit() for part in time_part), f"Время должно содержать только цифры: {time_part}"
    assert len(tz_part) == 2, f"Неверный формат часового пояса: {tz_part}"
    assert all(part.isdigit() for part in tz_part), f"Часовой пояс доджен содержать только цифры: {tz_part}"


# Тест-кейс 2: Создание избранного места с указанием всех допустимых цветов (по очереди)
def test_case_2():
    token = get_session_token()
    data = {
        "title": "Место с цветом",
        "lat": 45.46427,
        "lon": 9.18951,
        "color": "YELLOW"
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 200, f"Ожидался статус 200, но получили {response.status_code}"

    response_data = response.json()
    required_fields = ['id', 'title', 'lat', 'lon', 'color', 'created_at']

    for field in required_fields:
        assert field in response_data, f"Отсутствует поле: {field}"

    assert response_data['title'] == data['title']
    assert response_data['lat'] == data['lat']
    assert response_data['lon'] == data['lon']
    assert response_data['color'] == data['color']
    assert response_data['id'] > 0

    created_at = response_data['created_at']

    assert 'T' in created_at, f"Неверный формат даты: {created_at}"
    assert ':' in created_at, f"Неверный формат времени: {created_at}"

    parts = created_at.split('T')

    assert len(parts) == 2, f"Неверный формат даты"

    date_part = parts[0]
    time_part = parts[1]

    date_parts = date_part.split('-')
    assert len(date_parts) == 3, f"Неверный формат даты: {date_part}"
    assert all(part.isdigit() for part in date_parts), f"Дата должна содержать только цифры: {date_part}"

    time_part, tz_part = time_part.split('+')
    time_part = time_part.split(':')
    tz_part = tz_part.split(':')
    assert len(time_part) == 3, f"Неверный формат времени: {time_part}"
    assert all(part.isdigit() for part in time_part), f"Время должно содержать только цифры: {time_part}"
    assert len(tz_part) == 2, f"Неверный формат часового пояса: {tz_part}"
    assert all(part.isdigit() for part in tz_part), f"Часовой пояс доджен содержать только цифры: {tz_part}"

