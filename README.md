## Установка и запуск
1. Клонировать репозиторий
    ```
    git clone https://github.com/wertwu/CRUD
    ```
2. Перейдите в директорию CRUD
    ```
   cd CRUD
    ```
3. Создать виртуальное окружение и установить зависимости
    ``` 
   python -m venv venv
    ```
   Варианты активации окружения:
   - windows ``` venv/Scripts/activate ```
   - linux ``` venv/bin/activate ```
     <br><br>
   ```
   python -m pip install -U pip
   ```
   ```
   pip install -r requirements.txt
   ```
4. Выполните миграции
   ```
   python manage.py migrate
   ```
5. Создать суперюзера
   ```
   python manage.py createsuperuser
   ```
6. Запустить приложение на сервере разработчика
   ```
   python manage.py runserver
   ```
7. Проект доступен ```http://localhost:8000/```

 ### Функции
- **POST**```/api-token-auth/``` Получить токен
```
{
  "username": "string",
  "password": "string"
}
```
- **GET**```/api/users/```  Список всех пользователей
- **POST**```/api/users/``` Создание нового пользователя
```
{
  "username": "string",
  "first_name": "string",
  "last_name": "string",
  "password": "string",
  "is_active": true
}
```
- **GET**```/api/users/"id"/``` Просмотр данных пользователя
- **PUT**```/api/users/"id"/``` Редактирование данных пользователя
```
{
  "username": "string",
  "first_name": "string",
  "last_name": "string",
  "password": "string",
  "is_active": true
}
```
- **DELETE**```/api/users/"id"/``` Удаление пользователя
