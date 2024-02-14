install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

build:
	poetry build

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck test lint

selfcheck:
	poetry check

.PHONY: install test lint selfcheck check build
