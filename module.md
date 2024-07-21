# Документация к модулю

## krrsnkapi.KrrsnkAPI.KrrsnkCHAT
Это пока что единственное что тут есть :3 

### Отправка сообщений
Отправка осуществляется через функцию send_message в классе KrrsnkCHAT

Пример использования:
```python
from krrsnkapi import KrrsnkAPI

api = KrrsnkAPI("Тут ключ")


api.KrrsnkCHAT.send_message("Тут сообщение", "Тут юзернейм (опционально, по умолчанию стоит имя ключа)")

# Пример чтоб ошибки не лепило если что
import krrsnkapi

try:
    api.KrrsnkCHAT.send_message("Тут тоже самое")
except krrsnkapi.KrrsnkAPIError as e:
    print(f"Произошла ошибка: {e}")
```

### Получение сообщений
Это осуществляется через функцию get_messages в том же классе

Пример:
```python
from krrsnkapi import KrrsnkAPI

api = KrrsnkAPI("Тут ключ")


messages = api.KrrsnkCHAT.get_messages() # Вернёт словарь

# Пример как это можно сделать читаемым

for message in messages:
    print(f"{message['created_at']} {message['sender']} (ID: {message['sender_id']}) : {message['message']}\nMessage ID: {message['id']}\n\n")
```

#### Получения по айди
Тут практически тоже самое, только get_messages() будет уже как get_message_by_id()

Пример:
```python
from krrsnkapi import KrrsnkAPI

api = KrrsnkAPI("Тут ключ")


message = api.KrrsnkCHAT.get_message_by_id(1) # Вместо 1 можно любое число. Вернёт словарь

# Вывод сообщения
print(f"{message['created_at']} {message['sender']} (ID: {message['sender_id']}) : {message['message']}\nMessage ID: {message['id']}\n\n")
```
