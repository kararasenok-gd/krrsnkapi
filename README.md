# krrsnk-api
Простой способ использования моего API

P.S На моём [Boosty](https://boosty.to/kararasenok_gd) есть исходники так и api, так и модуля
## Получение ключа
1. [Авторизуемся](https://kararasenok.ueuo.com/accounts/login.php) (если надо [регестрируемся](https://kararasenok.ueuo.com/accounts/register.php))
2. [Переходим](https://kararasenok.ueuo.com/api/create/) и создаём ключ
3. Полученый ключ куда нибудь сохраняем
4. Готово!
## Примеры
### Пример 1: Взаимодействие с [Чатом](https://kararasenok.ueuo.com/tests/phpchat)

Я добавил возможность взаимодествия с чатом. Вот пример:

```python
from krrsnkapi import Chat

message = input("Сообщение для отправки: ")

status = Chat("ваш API ключ").send_message(message)

if status == "MESSAGE_ADDED":
    print("Отправлено!")
elif status == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print("Неизвестная ошибка")
```

Так же можно получить полную информацию о последнем сообщении.

```python
from krrsnkapi import Chat

info = Chat("ваш API ключ").get_last_message_info("id") # Вместо id можно указать это: id - id сообщения | sender - имя отправителя | sender_id - айди отправителя | message - сообщение | created_at - когда отправлено

if info == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print(info)
```

Также можно получить сообщение по его айди

```python
from krrsnkapi import Chat

message = Chat("ваш API ключ").get_message_by_id("151") # Вместо 151 можно указать любой другой айди | так же можно указать чтоб вернуло только сообщение, для этого можно прописать returnMessage = "1" или просто "1" после айди (по умолчанию: returnMessage = "0")

if message == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print(message)
```

### Пример 2: Base64

Тут также есть декодер и энкодер Base64, вот пример декодера:

```python
from krrsnkapi import Base64

message = input("Текст для декодирования: ")

status = Base64("ваш API ключ").decode(message)

if status == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print(status)
```

А вот энкодера:

```python
from krrsnkapi import Base64

message = input("Текст для декодирования: ")

status = Base64("ваш API ключ").decode(message)

if status == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print(status)
```
