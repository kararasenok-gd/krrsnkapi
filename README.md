# !!!
В скором времени апи переедет на вторую версию и 1 станет недоступной

# krrsnk-api
Простой способ использования моего API

P.S На моём [Boosty](https://boosty.to/kararasenok_gd) есть исходники первых версий api
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

Либо информацию

```python
from krrsnkapi import Chat

info = Chat("ваш API ключ").get_message_info_by_id("151", "id") # Тут как и в случае с get_last_message_info, вместо id что то из перечисленного ранее. И вместо 151 как и в случае с get_message_by_id заменить на любое другое айди

if info == "KEY_NOT_FOUND":
    print("Ключ не найден")
else:
    print(info)
```

### Пример 2: Песочница PHP
Ну тут обьяснять не надо. Я думаю...
```python
from krrsnkapi import PHPsandbox
code = "echo 'Hello, World!';"
status = PHPsandbox("ключ").create_code(code) # Называеться create_code потому, что то, что указано в функции создаёт скрипт на сайте и возвращает ссылку на исполнение кода
print(status)
```
### Пример 3: R34
Будет возвращать рандомную ссылку с rule34.xxx
```python
from krrsnkapi import r34
url = r34("ключ").get_url("omori", 1) # Вместо omori можно что то другое (это тег(-и), или как в модуле - keyword), а вместо 1, любое другое число (это страница, или как в модуле - page)
print(url)
```
Или можно побыстрее (напрямую)
```python
# Ключ можешь не изменять, он не проверяется :D
from krrsnkapi import r34
json = r34("ключ").get_url("omori", 1, True) # Вместо omori можно что то другое (это тег(-и), или как в модуле - keyword), а вместо 1, любое другое число (это страница, или как в модуле - page)
url = r34("ключ").get_img_link(json)
print(url)
```
