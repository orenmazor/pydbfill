test:
	docker-compose up
	docker-compose run runner poetry run pytest
