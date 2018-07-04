# Agata Project - Azazel

## Description

Um webservice para o backend da semana da computação.

## Motivation

## Table of Contents

* [Environment](#environment)
  * [Dependences](#environment-dependences)
  * [Variables](#environment-variables)
* [Development](#development)
* [Run](#run)
* [Version History](#version-history)
* [License](#license)

## Environment

### Environment Dependences

* Postgresql 10.4
* Python 3.6.5
* pyenv
* pipenv

### Environment Variables

[TODO]

## Development

```sh
cp env.example .env
cd azazel
```

```sh
pipenv run migrate
pipenv run createsuperuser
```

## Run

```sh
pipenv run server
```

## Version History

See [CHANGELOG.md](https://github.com/agata-project/azazel/blob/master/CHANGELOG.md)

## License

[LICENCE](https://github.com/agata-project/azazel/blob/master/LICENSE)
