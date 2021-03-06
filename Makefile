init:
	pip install -r requirements.txt

test:
	python -m pytest --cov-report term-missing:skip-covered --cov=src/ tests/

test-coverage-report:
	python -m pytest --cov-report term-missing:skip-covered \
		--cov-report html:htmlcov \
		--cov=src/ tests/

lint:
	pylint 

env:
	pipenv shell

clean:
	rm -rf htmlcov
	
.PHONY: init test test-coverage-report env