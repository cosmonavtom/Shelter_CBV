# Django-project: "Shelter_CBV"

## Краткое описание

Проект сохраняет, изменяет, отображает и удаляет данные по собакам в питомнике.
Имеется поиск по собакам и подсчёт кол-во просмотров отдельных собак.
Доступна регистрация пользователей с фидбеком на почту.

Для проекта используется виртуальное окружение venv

1) Необходимые для установки файлы прописаны в requirements.txt
```bash
pip install -r requirements.txt
```
2) Для подключения БД смотри env_sample
3) Команда для создания БД - ccdb
```bash
python manage.py ccdb
```
4) Команда для создания админа, модератора и юзера - ccsu
```bash
python manage.py ccsu
```
5) Создайте и проведите миграции
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
6) Запустите redis-server в отдельной вкладке терминала
```bash
redis-server
```
7) Теперь можно запустить сам сервер
```bash
python manage.py runserver
```

## Расшифровка env-файла
MS_SQL_USER= имя пользователя в ДБ

MS_SQL_SERVER= сервер

MS_SQL_DATABASE= название ДБ

MS_SQL_KEY= пароль в ДБ


CACHE_ENABLED= кеширование (TRUE)

CACHE_LOCATION=redis://127.0.0.1:6379


YANDEX_PASSWORD_APP= пароль для рассылки из YANDEX

EMAIL_HOST_USER= почта на яндексе откуда будет производиться рассылка


