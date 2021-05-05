# poll-service

## Setup API:

1. Build docker image:

```shell
docker-compose build poll-service-api
```

2. Run unittests:
```shell
docker-compose run --rm -e DJANGO_SETTINGS_MODULE=poll_service.unittest poll-service-api ./manage.py test
```

3. Run Django migration:

```shell
docker-compose run --rm poll-service-api ./manage.py migrate
```

4. Create admin user:

```shell
docker-compose run --rm poll-service-api ./manage.py createsuperuser
```

5. Run poll-service:

```shell
docker-compose run --rm poll-service-api ./manage.py runserver 0.0.0.0:8000
```

6. Open http://localhost:8000/admin/ in your browser, login as administrator user and create a few polls.


7. Review OpenApi schema http://localhost:8000/api/schema/swagger-ui/


8. Make request to get polls:

```shell
curl http://localhost:8000/api/v1/polls/
```

9. Add answers for a poll (just example):
```shell
curl --request POST \
  --url http://localhost:8000/api/v1/pass_poll/ \
  --header 'Content-Type: application/json' \
  --data '{
    "poll_id": 1,
    "answers": [
        {"question_id": 1, "text_answer": "free text"}
    ]
}'
```
