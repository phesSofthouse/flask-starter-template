# Flask Starter Template
A bare minimum flask starter template.

## Development

### Quickstart

Start a development server of flask-starter-template with the following command:

    flask --app flask-starter-template run --debug

### Requirements

#### Install requirements

Required dependencies:

    pip install -r requirements/requirements.txt

Dev dependencies:

    pip install -r requirements/dev.txt

##### Update requirements
If a dependency is to be added to the project, add it to the appropriate .in file and run:

    pip-compile requirements/path-to-file.in

##### Sync local virtual environment with requirements
If you would like to sync your local virtual environment with the generated and locked requirements of the project, run:

    pip-sync requirements/path-to-file.in


### Run tests

    python -m unittest

### Pre-commit hooks

It is recommended that every developer working on this project activate pre-commit hooks.

#### Activate pre-commit hooks
    pre-commit install
