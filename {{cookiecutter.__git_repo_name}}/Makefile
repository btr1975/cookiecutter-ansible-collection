# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.1
#

.PHONY: all info coverage pytest black yamllint check-security check-vuln

info:
	@echo "make options"
	@echo "    black             To format code with black"
	@echo "    coverage          To run coverage and display ASCII and output to htmlcov"
	@echo "    pytest            To run pytest with verbose option"
	@echo "    yamllint          To lint yaml"
	@echo "    check-vuln        To check for vulnerabilities in the dependencies"
	@echo "    check-security    To check for vulnerabilities in the code"

all: black yamllint coverage check-security check-vuln

coverage:
	@pytest --cov --cov-report=html -vvv

pytest:
	@pytest --cov -vvv

black:
	@black plugins/
	@black tests/

yamllint:
	@yamllint ./

check-vuln:
	@pip-audit -r requirements.txt

check-security:
	@bandit -c pyproject.toml -r .
