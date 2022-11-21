update:
	poetry update

install:
	poetry install

docker-install:
	docker build -t stripe_payment_test .

start:
	poetry run python manage.py runserver

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

lint:
	poetry run flake8 stripe_payment_test payment users payment users

secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

createsuperuser:
	poetry run python manage.py createsuperuser
