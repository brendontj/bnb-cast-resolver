SHELL := bash
PYTHON := python3
PIP := pip3

.DEFAULT_GOAL := elenco
.PHONY := install clean purge

venv:
	virtualenv -p $(PYTHON) $@

install: venv
	source $</bin/activate && $(PIP) install -r requirements.txt

elenco: venv install
	echo '#! /usr/bin/env bash' > elenco
	echo 'source $</bin/activate' >> elenco
	echo 'python3 ./src/main.py $${@:1}' >> elenco
	echo 'deactivate' >> elenco
	chmod a+x elenco

clean:
	-rm elenco 2&> /dev/null || true

purge: clean
	-rm -rf venv 2&> /dev/null || true