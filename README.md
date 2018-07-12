# Agata Project - Azazel

![Azazel](https://img.shields.io/badge/agata--project-azazel-blue.svg)
[![TravisCi](https://travis-ci.org/agata-project/azazel.svg?branch=master)](https://travis-ci.org/agata-project/azazel)
[![Ebert](https://ebertapp.io/github/agata-project/azazel.svg)](https://ebertapp.io/github/agata-project/azazel)

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

cp .env.example .env

## Development

### Create DB

```sh
pipenv run setupdbdev
pipenv run setupdbtest
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
