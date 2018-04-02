init:
	pip install -r requirements.txt

test:
	python -m pytest tests/

venv:
	python -m venv . 
	
.PHONY: init test venv