dev:
	pip install -r backend/requirements.txt
	cd frontend && npm install

migrate:
	python backend/manage.py makemigrations
	python backend/manage.py migrate

run:
	npm run --prefix frontend dev & pipenv run python backend/manage.py runserver
