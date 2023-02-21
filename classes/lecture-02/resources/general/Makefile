PIP := venv/bin/pip
PYTHON3 := venv/bin/python3

clear:
	rm -rf venv

venv:
	python3 -m venv venv

requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} main.py

setup:
	make clear
	make venv
	make requirements
