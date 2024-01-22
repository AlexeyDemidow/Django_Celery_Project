# Тестовая рассылка сообщений на базе Django, Celery и redis

Проект создан для изучения основ Celery в связке с Django.<br>

## Нюансы
- Redis запускался в docker-контейнере по команде:<br>
``docker run -d -p 6379:6379 redis``<br>
- Для ОС Windows ``REDIS_HOST`` должен быть равен ``'localhost'``
- Также для ОС Windows для выполнения задач нужно подключить eventlet:<br>
``pip install eventlet``<br>
И запускать worker командой:<br>
``celery -A proj-name worker -l info -P eventlet``
