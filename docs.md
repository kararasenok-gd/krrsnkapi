# API Документация

## Основной URL

```
https://kararasenok.ueuo.com/api/v2
```

## На заметку
ДАЖЕ НЕ ПЫТАЙТЕСЬ ПОЛУЧИТЬ КОД СОСТОЯНИЯ ЧЕРЕЗ status_code (requests Python), он везде будет 200. Получайте его из выданных сервером данных (code)

## Ограничения
Все эндпоинты имеют ограничения: не больше 5 запросов в минуту. Если привысить этот лимит. Будет ошибка

- Код состояния: 429 Too Many Requests
- Тело ответа:

```json
{
    "error": "You have reached the rate limit. Please wait a few seconds and try again.",
    "code": 429
}
```

## Раздел: krrsnkchat

## Эндпоинты

### 1. Добавить сообщение

```
POST /krrsnkchat/add.php
```

#### Описание

Добавляет новое сообщение в чат.

#### Параметры запроса

- `key` (обязательный) - API ключ для авторизации.
- `message` (обязательный) - Текст сообщения.
- `username` (опционально) - Имя отправителя (если не указать, будет указано имя ключа).

#### Тело запроса

```json
{
    "key": "your_api_key",
    "message": "Your message text",
    "username": "YourUsername"
}
```

#### Ответ

**Успешный ответ:**

- Код состояния: 200 OK
- Тело ответа:

```json
{
    "success": "Message added",
    "code": 200
}
```

**Ошибка:**

- Код состояния: 401 Unauthorized
- Тело ответа:

```json
{
    "error": "Key not found",
    "code": 401
}
```

- Код состояния: 400 Bad Request
- Тело ответа:

```json
{
    "error": "Missing parameters",
    "code": 400
}
```

### 2. Получить все сообщения

```
POST /krrsnkchat/get.php
```

#### Описание

#### Параметры запроса

- `key` (обязательный) - API ключ для авторизации.

#### Тело запроса

```json
{
    "key": "your_api_key"
}
```

#### Ответ

**Успешный ответ:**

- Код состояния: 200 OK
- Тело ответа:

```json
{
  "messages": [
    {
      "id": "1",
      "sender": "User1",
      "sender_id": "1",
      "message": "Message",
      "created_at": "2024-07-21 18:50:17"
    },
    {
      "id": "2",
      "sender": "User2",
      "sender_id": "2",
      "message": "Message",
      "created_at": "2024-07-21 18:51:32"
    }
  ],
  "code": 200
}
```

**Ошибка:**

- Код состояния: 401 Unauthorized
- Тело ответа:

```json
{
    "error": "Key not found",
    "code": 401
}
```

- Код состояния: 400 Bad Request
- Тело ответа:

```json
{
    "error": "Missing parameters",
    "code": 400
}
```

### 3. Получить сообщение по ID

```
POST /krrsnkchat/getByID.php
```

#### Описание

Получает сообщение по его идентификатору.

#### Параметры запроса

- `key` (обязательный) - API ключ для авторизации.
- `id` (обязательный) - Идентификатор сообщения.

#### Тело запроса

```json
{
    "key": "your_api_key",
    "id": 1
}
```

#### Ответ

**Успешный ответ:**

- Код состояния: 200 OK
- Тело ответа:

```json
{
  "message": {
    "id": "1",
    "sender": "User1",
    "sender_id": "1",
    "message": "Message",
    "created_at": "2024-07-21 18:50:17"
  },
  "code": 200
}
```

**Ошибка:**

- Код состояния: 401 Unauthorized
- Тело ответа:

```json
{
    "error": "Key not found",
    "code": 401
}
```

- Код состояния: 404 Not Found
- Тело ответа:

```json
{
    "error": "Message not found",
    "code": 404
}
```

## Ошибки

- `400 Bad Request` - Некорректные параметры запроса или тела запроса.
- `401 Unauthorized` - Некорректный или отсутствующий API ключ.
- `404 Not Found` - Ресурс не найден.
- `500 Internal Server Error` - Ошибка на сервере.

## Примеры использования

### Добавить сообщение

```bash
curl -X POST "https://kararasenok.ueuo.com/api/v2/krrsnkchat/add.php" -H "Content-Type: application/json" -d '{"key": "your_api_key", "message": "New message", "username": "YourUsername"}'
```

### Получить все сообщения

```bash
curl -X POST "https://kararasenok.ueuo.com/api/v2/krrsnkchat/get.php" -H "Content-Type: application/json" -d '{"key": "your_api_key"}'
```

### Получить сообщение по ID

```bash
curl -X POST "https://kararasenok.ueuo.com/api/v2/krrsnkchat/getByID.php" -H "Content-Type: application/json" -d '{"key": "your_api_key", "id": 1}'
```
