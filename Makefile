install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish: build
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

reinstall:
	python3 -m pip install --force-reinstall dist/*.whl