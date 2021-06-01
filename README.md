# fastapi_test
**Тестовое задание: Настройка**
Для запуска проекта необходимо:
- Создать  базу данных `Postgresql` с названием "test_task"
- в файле `database.py` в переменную `engine` вставить необходимые данные:
("postgresql+psycopg2://postgres:1234@localhost/test_task")
("postgresql+psycopg2://имя_пользователя:пароль@хост/имя_базы")
- в командной строке ввести: `pip install -r requirements.txt`

**Запуск**
- Для запуска,в  командную строчку вставить: `uvicorn main:app --reload --port 5050`
- После в открыть браузер и перейти по такой ссылке: `http://127.0.0.1:5050/docs`

