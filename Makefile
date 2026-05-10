.PHONY: install test security coverage clean build upload

install:
	pip install -e .

test:
	python run_all_tests.py

security:
	python -m unittest discover tests/security -v

coverage:
	coverage run --source=src/sir_simulator -m unittest discover tests
	coverage report
	coverage html

clean:
	rm -rf dist build *.egg-info coverage_html_report .coverage

build:
	python -m build

upload:
	twine upload dist/*

all: clean install test security coverage build
