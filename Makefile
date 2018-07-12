init:
    pip install pipenv
    pipenv install --dev

test:
    pipenv run py.test tests/ -v --cov azazel --cov-report term-missing
