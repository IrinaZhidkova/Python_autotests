import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e8489810485a2807d0eb3dcb4897be7a'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

# Создание покемона
body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
response_data = response_create.json()  # Сохраняем JSON-ответ

print(response_data)  # Чтобы видеть полный ответ в терминале

pokemon_id = response_data.get("id")  # Достаем ID покемона
message = response_data.get("message", "Сообщение отсутствует")

print(f"Создан покемон с ID: {pokemon_id}")
print(message)

# Проверяем, создался ли покемон
if not pokemon_id:
    print("Ошибка: Покемон не был создан. Остановка выполнения.")
    exit()

# Смена имени покемона
body_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print(response_change.text)

# Поймать покемона в покебол
body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print(response_catch.text)