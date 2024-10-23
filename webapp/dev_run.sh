
#!/usr/bin/env bash

poetry run black .
poetry run isort . --profile black
poetry run flake8 .
poetry run bandit .