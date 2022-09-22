coverage:
	coverage run --source=number_spell --branch -m pytest test
	coverage html -d coverage_html

install:
	pip install -r requirements.txt


install-dev: install
	pip install -e ".[dev]"

install-pip-tools:
	pip install pip-tools

freeze: install-pip-tools
	pip-compile -v --no-emit-index-url --output-file requirements.txt setup.py

test_integration:
	pytest -sv test/integration

test_unit:
	pytest -sv test/unit

mypy:
	mypy number_spell/ test/
    
.PHONY: test_integration install install-dev freeze install-pip-tools coverage mypy
