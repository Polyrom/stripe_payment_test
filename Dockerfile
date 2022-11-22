FROM python:3.8.10-slim

RUN apt-get update && apt-get install -yq make gettext

RUN pip3 install -U poetry
RUN poetry config virtualenvs.in-project true

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

CMD ["bash", "-c", "poetry run python manage.py migrate", "poetry run gunicorn stripe_payment_test.wsgi --log-file -"]
