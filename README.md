# Django REST Framework Todo List

Полнофункциональное приложение для управления задачами с JWT аутентификацией.

## ⚡ Быстрый старт

```bash
# Клонирование и переход в директорию
git clone <https://github.com/Anuar000/TaskManager.git>
cd todolist_project

# Установка зависимостей
pip install -r requirements.txt

# Создание базы данных
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

Приложение будет доступно по адресу: http://127.0.0.1:8000/

## 📋 Функциональность

### Пользователи
-  Регистрация с валидацией данных
-  Аутентификация через JWT токены
-  Автоматическое обновление токенов

###  Задачи
-  Создание задач с названием, описанием, статусом и сроком выполнения
-  Просмотр списка собственных задач
-  Фильтрация по статусу (new, in_progress, done)
-  Сортировка по дате создания и сроку выполнения
-  Поиск по названию и описанию
-  Обновление и удаление задач
-  Автоматическая пометка просроченных задач

##  API Документация

### Аутентификация

#### Регистрация пользователя
```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "strongpassword123",
    "password_confirm": "strongpassword123"
}
```

**Ответ:**
```json
{
    "user": {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com",
        "date_joined": "2025-06-20T10:00:00Z"
    },
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "message": "Пользователь успешно зарегистрирован"
}
```

#### Вход в систему
```http
POST /api/auth/login/
Content-Type: application/json

{
    "email": "john@example.com",
    "password": "strongpassword123"
}
```

#### Обновление токена
```http
POST /api/auth/token/refresh/
Content-Type: application/json

{
    "refresh": "your_refresh_token_here"
}
```

### Задачи

> **Важно:** Все запросы к задачам требуют заголовок авторизации:
> ```
> Authorization: Bearer your_access_token_here
> ```

#### Получение списка задач
```http
GET /api/tasks/
```

**Параметры фильтрации:**
- `?status=new` - фильтр по статусу (new, in_progress, done)
- `?ordering=-due_date` - сортировка по убыванию даты
- `?ordering=due_date` - сортировка по возрастанию даты
- `?search=покупки` - поиск по названию и описанию

**Пример запроса:**
```http
GET /api/tasks/?status=new&ordering=-due_date&search=покупки
```

**Ответ:**
```json
{
    "count": 25,
    "next": "http://127.0.0.1:8000/api/tasks/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Купить продукты",
            "description": "Молоко, хлеб, яйца",
            "status": "new",
            "due_date": "2025-06-21T18:00:00Z",
            "is_overdue": false,
            "created_at": "2025-06-20T10:00:00Z",
            "updated_at": "2025-06-20T10:00:00Z"
        }
    ]
}
```

#### Создание задачи
```http
POST /api/tasks/
Content-Type: application/json

{
    "title": "Подготовить презентацию",
    "description": "Презентация для клиента по новому проекту",
    "status": "new",
    "due_date": "2025-06-25T15:00:00Z"
}
```

#### Получение конкретной задачи
```http
GET /api/tasks/1/
```

#### Обновление задачи
```http
PUT /api/tasks/1/
Content-Type: application/json

{
    "title": "Подготовить презентацию (обновлено)",
    "description": "Презентация для клиента по новому проекту с дополнениями",
    "status": "in_progress",
    "due_date": "2025-06-25T15:00:00Z"
}
```

**Частичное обновление:**
```http
PATCH /api/tasks/1/
Content-Type: application/json

{
    "status": "done"
}
```

#### Удаление задачи
```http
DELETE /api/tasks/1/
```

## Статусы задач

| Статус | Значение | Описание |
|---------|----------|----------|
| `new` | Новая | Только что созданная задача |
| `in_progress` | В процессе | Задача в работе |
| `done` | Завершена | Задача выполнена |

## Обработка ошибок

Приложение возвращает следующие HTTP коды:

- **200** - Успешный запрос
- **201** - Ресурс создан
- **204** - Ресурс удален
- **400** - Ошибка валидации данных
- **401** - Не авторизован
- **404** - Ресурс не найден
- **500** - Внутренняя ошибка сервера

**Пример ошибки валидации:**
```json
{
    "error": "Название задачи должно содержать минимум 3 символа"
}
```

## Технические детали

### Требования
- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+
- SQLite (по умолчанию)

### Структура проекта
```
todolist_project/
├── todolist_project/      # Основные настройки проекта
├── users/                 # Приложение пользователей
├── tasks/                 # Приложение задач
├── requirements.txt       # Зависимости
├── manage.py             # Django утилита
└── README.md             # Документация
```

### Валидация данных

#### Пользователи
- Username: обязательное поле
- Email: уникальный, валидный email
- Пароль: проходит стандартную валидацию Django

#### Задачи
- Title: минимум 3 символа
- Due_date: не может быть в прошлом (для новых задач)
- Status: только из предустановленных вариантов

### Безопасность
- JWT токены с автоматическим обновлением
- Пользователи видят только свои задачи
- Валидация всех входящих данных

### Документация
- По желанию можно использовать swagger по адресу: http://127.0.0.1:8000/swagger
