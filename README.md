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

3. Review OpenApi schema:
```shell
browse http://localhost:8000/api/schema/swagger-ui/
```

4. Run Django migration:

```shell
docker-compose run --rm poll-service-api ./manage.py migrate
```

5. Create super user:

```shell
docker-compose run --rm poll-service-api ./manage.py createsuperuser
```

6. Create API user:

6.1. Open Django shell:
```shell
docker-compose run --rm poll-service-api ./manage.py shell
```
    
6.2. Type:
```
%cpaste
```
    
6.3. Copy the following code and paste to the Django shell:
```
from django.contrib.auth.models import User
user = User.objects.create(email='test@example.com', username='test@example.com')
user.set_password('1234')
user.save()
--
```

7. Run poll-service:

```shell
docker-compose run --rm poll-service-api ./manage.py runserver 0.0.0.0:8000
```

8. Open http://localhost:8000/admin/ in your browser, login as admin user and create a few polls.


9. Make request to get polls:

```shell
curl http://localhost:8000/api/v1/polls/
```

10. Add answers for a poll (just example):
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
