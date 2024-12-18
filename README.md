# Тестовое задание

## Использованный стек
* Django
* DRF
* Celery

## Функционал
По API запросу создает уведомление (celery task), которое отправляется (пишется в консоль) для каждого поставщика с с учетом его часового пояса.

Релизованы методы:
* /api/notifications/notifications/schedule - отправляет уведомление всем поставщикам на следующий день в 10 утра с учетом часового пояса области
* /api/notifications/notifications/now - отправляет уведомление всем поставщикам сразу в одно и тоже вермя

API Docs: /api/schema/swagger-ui/

## Запуск
```shell
docker run --rm -it \
    -e RABBITMQ_DEFAULT_USER=username \
    -e RABBITMQ_DEFAULT_PASS=password \
    -p 5672:5672 \
    rabbitmq:3                                                    # rabbitmq
pip install -r requirements.txt                                   # устанавливаем зависимости
python ./manage.py migrate                                        # применяем миграции
python ./manage.py loaddata notifications/fixtures/districts.json # применяем фикстуру областей
python ./manage.py loaddata notifications/fixtures/suppliers.json # применяем фикстуру поставщиков
python ./manage.py runserver                                      # запускаем веб-сервер
python -m celery -A conf.celery_app worker                        # запускаем celery worker в другой сессии
```
