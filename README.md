## Команды для запуска:

```bash
# 1. Создание проекта
django-admin startproject todolist_project
cd todolist_project

# 2. Создание приложений
python manage.py startapp users
python manage.py startapp tasks

# 3. Установка зависимостей
pip install -r requirements.txt

# 4. Создание и применение миграций
python manage.py makemigrations
python manage.py migrate

# 5. Создание суперпользователя
python manage.py createsuperuser

# 6. Запуск сервера
python manage.py runserver
```

## API Endpoints:

### Аутентификация:
- POST `/api/auth/register/` - Регистрация
- POST `/api/auth/login/` - Вход
- POST `/api/auth/token/refresh/` - Обновление токена

### Задачи:
- GET `/api/tasks/` - Список задач (с фильтрацией и сортировкой)
- POST `/api/tasks/` - Создание задачи  
- GET `/api/tasks/{id}/` - Получение задачи
- PUT/PATCH `/api/tasks/{id}/` - Обновление задачи
- DELETE `/api/tasks/{id}/` - Удаление задачи

## Параметры фильтрации:
- `?status=new|in_progress|done` - фильтр по статусу
- `?ordering=-due_date` - сортировка по дате (убывание)
- `?ordering=due_date` - сортировка по дате (возрастание)
- `?search=текст` - поиск по названию и описанию
