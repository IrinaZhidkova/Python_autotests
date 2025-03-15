import requests
import pytest  # Добавлено

# Константы
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8489810485a2807d0eb3dcb4897be7a'  # Замени на свой актуальный токен
HEADERS = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = "13114"  # Замени на свой ID

# 1️⃣ Проверка, что API /trainers возвращает статус 200
def test_status_code():
    response = requests.get(f'{URL}/trainers', headers=HEADERS)
    assert response.status_code == 200, f"Ошибка! Ожидался код 200, а получен {response.status_code}"

# 2️⃣ Проверка, что имя тренера есть в ответе
def test_trainer_name_in_response():
    params = {'trainer_id': TRAINER_ID}
    response = requests.get(f'{URL}/trainers', headers=HEADERS, params=params)
    
    assert response.status_code == 200, f"Ошибка! Ожидался код 200, а получен {response.status_code}"

    response_json = response.json()
    trainer_data = response_json.get("data", [])

    assert any(trainer.get("id") == TRAINER_ID for trainer in trainer_data), "Ошибка! Тренер не найден в ответе"