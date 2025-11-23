import pytest
import requests
import time


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
@pytest.mark.parametrize('colors', ['BLUE', 'GREEN', 'RED', 'YELLOW'])
def test_case_2(colors):
    token = get_session_token()
    data = {
        "title": "Место с цветом",
        "lat": 45.46427,
        "lon": 9.18951,
        "color": colors
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


# Тест-кейс 3: Создание избранного места с минимальной длиной названия
def test_case_3():
    token = get_session_token()

    data = {
        "title": "1",
        "lat": 40.85216,
        "lon": 14.26811
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


# Тест-кейс 4: Создание избранного места с максимальной длиной названия (999 символов)
def test_case_4():
    long_string = "Q" * 200 + "w" * 200 + "У" * 200 + "к" * 100 + "." * 100 + "," * 198 + "7"
    token = get_session_token()

    data = {
        "title": long_string,
        "lat": 40.85216,
        "lon": 14.26811
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


# Тест-кейс 5: Попытка создания избранного места сo спецсимволами в названии
def test_case_5():
    token = get_session_token()

    data = {
        "title": "Бар+ 'Лучшее&Point' №1!",
        "lat": 45.07049,
        "lon": 7.68682
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert 'error' in response.json()


# Тест-кейс 6: Создание избранного места с граничными значениями координат
def test_case_6():
    token = get_session_token()

    data = {
        "title": "Граничные координаты",
        "lat": 90.0,
        "lon": 180.0
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


# Тест-кейс 7: Создание избранного места с отрицательными координатами
def test_case_7():
    token = get_session_token()

    data = {
        "title": "Отрицательные координаты",
        "lat": -90.0,
        "lon": -180.0
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


# Тест-кейс 8: Создание избранного места с нулевыми координатами
def test_case_8():
    token = get_session_token()

    data = {
        "title": "Нулевые координаты",
        "lat": 0.0,
        "lon": 0.0
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


# Тест-кейс 9: Попытка создания избранного места без указания сессионного токена
def test_case_9():
    data = {
        "title": "Без токена",
        "lat": 44.49381,
        "lon": 11.33875
    }
    headers = {}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 401, f"Ожидался статус 401, но получили {response.status_code}"
    assert response.json()['error']['message'] == "Параметр 'token' является обязательным"


# Тест-кейс 10: Попытка создания избранного места с недействительным токеном
def test_case_10():
    token = get_session_token()
    time.sleep(2.1)
    data = {
        "title": "Токен недействителен",
        "lat": 44.49381,
        "lon": 11.33875
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 401, f"Ожидался статус 401, но получили {response.status_code}"
    assert 'error' in response.json()


# Тест-кейс 11: Попытка создания избранного места без указания обязательного поля title
def test_case_11():
    token = get_session_token()
    data = {
        "lat": 43.77925,
        "lon": 11.24626
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert 'error' in response.json()
    assert response.json()['error']['message'] == "Параметр 'title' является обязательным"


# Тест-кейс 12: Попытка создания избранного места без указания обязательного поля lat и/или lon
def test_case_12():
    token = get_session_token()
    data = {
        "title": "Не заполнены все обязательные поля"
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert response.json()['error']['message'] == "Параметры 'lat' и 'lon' являются обязательными"


# Тест-кейс 13: Попытка создания избранного места с пустым title
def test_case_13():
    token = get_session_token()
    data = {
        "title": "",
        "lat": 43.77925,
        "lon": 11.24626
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert response.json()['error']['message'] == "Параметр 'title' не может быть пустым"


# Тест-кейс 14: Попытка создания избранного места с невалидным значением color
def test_case_14():
    token = get_session_token()
    data = {
        "title": "Недопустимый цвет",
        "lat": 43.77925,
        "lon": 11.24626,
        "color": "INVALID_COLOR"
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )
    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert response.json()['error'][
               'message'] == "Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW"


# Тест-кейс 15: Попытка создания избранного места с title длиной 1000 символов
def test_case_15():
    token = get_session_token()
    string_1000 = "Q" * 200 + "w" * 200 + "У" * 200 + "к" * 100 + "." * 100 + "," * 100 + "1" * 100
    data = {
        "title": string_1000,
        "lat": 43.77925,
        "lon": 11.24626
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )

    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert 'error' in response.json()


# Тест-кейс 16: Попытка получения сессионного токена при отправке непустого тела запроса
def test_case_16():
    data = {"test": "test"}
    response = requests.post('https://regions-test.2gis.com/v1/auth/tokens', data=data)
    token = response.cookies.get('token')

    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert token is None, f"Токен не должен выдаваться, но получен: {token}"


# Тест-кейс 17: Попытка создания избранного места с lat и/или lon заполнеными некорректными типами данных
# (передаем не float, а float в виде строки)
def test_case_17():
    token = get_session_token()

    data = {
        "title": "Некорректные типы данных 1",
        "lat": "41.89193",
        "lon": "12.51133"
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )

    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert 'error' in response.json()


# Тест-кейс 18: Попытка создания избранного места с lat и/или lon заполненными некорректными типами данных
# (передаем строки)
def test_case_18():
    token = get_session_token()

    data = {
        "title": "Некорректные типы данных 2",
        "lat": "41.89193",
        "lon": "двадцать три"
    }
    headers = {'Cookie': f'token={token}'}
    response = requests.post(
        'https://regions-test.2gis.com/v1/favorites',
        data=data,
        headers=headers
    )

    assert response.status_code == 400, f"Ожидался статус 400, но получили {response.status_code}"
    assert response.json()['error']['message'] == "Параметр 'lon' должен быть числом"
