.PHONY: up
up:
	@docker-compose up --build -d

.PHONY: down
down:
	@docker-compose down

.PHONY: makemigrations
makemigrations:
	@docker exec library-api python manage.py makemigrations --noinput

.PHONY: migrate
migrate:
	@docker exec library-api python manage.py migrate --noinput

.PHONY: createuser
createuser:
	@docker exec library-api python manage.py createsuperuser --noinput
