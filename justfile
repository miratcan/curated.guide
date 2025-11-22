# curated.guide - Task runner

# Run development server
dev:
    uv run --directory src/backend python manage.py runserver

# Run migrations
migrate:
    uv run --directory src/backend python manage.py migrate

# Create migrations
makemigrations:
    uv run --directory src/backend python manage.py makemigrations

# Create superuser
superuser:
    uv run --directory src/backend python manage.py createsuperuser

# Django shell
shell:
    uv run --directory src/backend python manage.py shell

# Run tests
test:
    uv run --directory src/backend python manage.py test

# Format code
fmt:
    uv run ruff format .

# Lint code
lint:
    uv run ruff check .

# Install dependencies
install:
    uv sync
