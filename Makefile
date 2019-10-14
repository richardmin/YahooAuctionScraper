init:
	pip install -r requirements.txt

test:
	python3 -m pytest tests/

venv:
	pipenv shell
	
.PHONY: init test venv