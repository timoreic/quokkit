SHELL := /bin/bash

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
		@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
	
# target: activate - activate the virtual environment
activate:
		pipenv shell

# target: install - install requirements
install:
		pipenv install

# target: run - Run the application
run:
		python manage.py runserver

# target: test - Runs tests and check coverage
test:
		coverage run --source='.' manage.py test */tests

# target: coverage - Create a coverage report
coverage:
		coverage html

# target: migration - calls the "makemigrations" django command
migration:
		python manage.py makemigrations

# target: migrate - calls the "migrate" django command
migrate:
		python manage.py migrate

# target: superuser - calls the "createsuperuser" django command
superuser:
		python manage.py createsuperuser

# target: lint - Lint with flake8
lint:
		flake8