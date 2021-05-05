# poll-service

## Setup API:

1. Build docker image:

```shell
docker-compose build poll-service-api
```

2. Run Django migration:

```shell
docker-compose run --rm poll-service-api ./manage.py migrate
```

3. Create super user:

```shell
docker-compose run --rm poll-service-api ./manage.py createsuperuser
```

4. Create API user:

4.1. Open Django shell:
```shell
docker-compose run --rm poll-service-api ./manage.py shell
```

4.2. Type:
```
%cpaste
```

4.3. Copy the following code and paste to the Django shell:
```
from django.contrib.auth.models import User
user = User.objects.create(email='test@example.com', username='test@example.com')
user.set_password('1234')
user.save()
```

4.4. Type the following and press Enter: 
```
--
```
