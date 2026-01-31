dev:
	uv run app/manage.py runserver

migrate:
	uv run app/manage.py makemigrations

push:
	uv run app/manage.py migrate
