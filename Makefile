update:
	poetry update

install:
	poetry install

start:
	poetry run python manage.py runserver

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

lint:
	poetry run flake8 stripe_payment_test payment users payment users
