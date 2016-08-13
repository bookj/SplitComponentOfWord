.PHONY: create-venv

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

# CONFIG
PACKAGE_NAME := simple_calculator

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

create-venv: ## Create a virtual environment for python
	python -m venv venv

develop: ## Setup develop environment
	python setup.py develop

test: ## Test all codes with coverage
	nosetests --rednose --with-coverage --cover-erase --cover-package=$(PACKAGE_NAME) -v tests/*
