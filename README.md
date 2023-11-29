## Тестовое задание для компании Воронин

## Задание
Создать Django-приложение для управления книгами. Реализовать REST API для CRUD операций над книгами. Создать модель для хранения информации о пользователях, создать эндпойнт для регистрации новых пользователей. Реализовать асинхронную задачу для отправки приветственного электронного письма при регистрации. Создать две ветки в гите, сделать для них пул реквесты, убедиться, что они проходят тесты. Упаковать все в Docker.

## Решение
В решении использованы Django, DjangoRestFramework, база данных MySQL, Celery, Redis, Pytest, Docker, Github Actions. Для регистрации новых пользователей была расширена модель AbstractBaseUser, для нее написан собственный менеджер, также был реализован эндпойнт для регистрации пользователя. С помощью Celery была реализована асинхронная задача, которая выполняется при сохранении нового пользователя в БД. Был разработан с помощью DRF viewset для CRUD операций над книгами. Были написаны тесты для API с использованием Pytest и Factory Boy, также реализован с помощью Github Actions workflow, который автоматически прогоняет тесты при пул реквестах. Приложение можно запустить с помощью Docker-а

## API endpoints
**api/books/** endpoint для post и get(list) запросов. Post запрос должен содержать name, author, year_published, isbn

**api/books/{id}** endpoint для put, patch и get(retrieve) запросов. Put запрос должен содержать name, author, year_published, isbn; patch любое из этих полей.

**users/** endpoint для post запроса для регистрации нового пользователя. Тело должно содержать username, email, password


## Запус приложения

### Запуск приложения с помощью Docker
В корне проекта создайте **.env** файл и пропишите в нем следующие переменные:
```
DB_NAME=testdb
DB_USER=root
DB_PASSWORD=root
DB_HOST=db

CELERY_HOST_NAME=redis

EMAIL=*укажите email с которого будут отправляться письма*
EMAIL_PASSWORD=*ваш пароль*
```
Затем мы запускаем приложение следующей Docker командой в терминале:
```
docker-compose up -d
```
Приложение запуститься и должно быть доступно по локальному адресу [127.0.0.1:8000](http://127.0.0.1:8000)

Остановить приложение/запустить заново:
```
docker-compose stop
docker-compose start
```
Остановить приложение и удалить все связанные контейнеры, включая базу данных:
```
docker-compose down -v
```
При изменениях в коде проекта, необходимо заново создать образ и запустить сервисы:
```
docker-compose build
docker-compose up -d
```
Посмотреть все запущенные контейнеры:
```
docker ps
```
Посмотреть логи внутри определенного контейнера:
```
docker logs *название контейнера*
```
### Запуск приложения без использования Docker
Сначала в корне проекта создадим виртуальное окружение и активируем его:
```
python3 -m venv venv
source venv/bin/activate
```
Затем установим все зависимости проекта, отдав следующую команду:
```
pip install -r requirements.txt
```
После этого в корне проекта создайте **.env** файл и пропишите в нем следующие переменные:
```
DB_NAME=*название вашей базы*
DB_USER=*имя пользователя*
DB_PASSWORD=*пароль*
DB_HOST=localhost

CELERY_HOST_NAME=localhost

EMAIL=*укажите email с которого будут отправляться письма*
EMAIL_PASSWORD=*ваш пароль*
```
***Убедитесь, что MySQL и Redis запущены на локальной машине***

Затем в корне проекта отдаем следующие команды, применяя миграции к базе данных:
```
python3 manage.py migrate
```
После этого можно запускать сервер следующей командой:
```
python3 manage.py runserver
```
Создаем Celery worker-а:
```
celery -A test_voronin worker --loglevel=INFO
```
Приложение запуститься и должно быть доступно по локальному адресу [127.0.0.1:8000](http://127.0.0.1:8000)

Прогнать тесты можно следующей командой:
```
pytest
```