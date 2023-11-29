FROM python:3.11.0-alpine

WORKDIR /app

COPY ./poetry.lock .
COPY ./pyproject.toml .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./library /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
