# krrsnk-api
Простой способ использования моего API
## Получение ключа
1. [Авторизуемся](https://kararasenok.ueuo.com/accounts/login.php) (если надо [регестрируемся](https://kararasenok.ueuo.com/accounts/register.php))
2. [Переходим](https://kararasenok.ueuo.com/api/create/) и создаём ключ
3. Полученый ключ куда нибудь сохраняем
4. Готово!
## Примеры
### Пример 1: Взаимодействие с [Чатом](https://kararasenok.ueuo.com/tests/phpchat)

Я добавил возможность взаимодествия с чатом. Вот пример:

```python
from krrsnk-api import Chat

message = input("Сообщение для отправки: ")

status = Chat("ваш API ключ").send_message(message)

if status == "MESSAGE_ADDED":
    print("Отправлено!")
elif status == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print("Неизвестная ошибка")
```

### Пример 2: Base64

Тут также есть декодер и энкодер Base64, вот пример декодера:

```python
from krrsnk-api import Base64

message = input("Текст для декодирования: ")

status = Base64("ваш API ключ").decode(message)

if status == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print(status)
```

А вот энкодера:

```python
from krrsnk-api import Base64

message = input("Текст для декодирования: ")

status = Base64("ваш API ключ").decode(message)

if status == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print(status)
```
