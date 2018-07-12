# Agata Project - Azazel

![Travis](https://img.shields.io/travis/agata-project/azazel.svg)
[![Build Status](https://travis-ci.org/agata-project/azazel.svg?branch=master)](https://travis-ci.org/agata-project/azazel)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/50694d9b57c642f4b8aa6190e6b8cd3f)](https://www.codacy.com/app/cuzikjack/azazel?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=agata-project/azazel&amp;utm_campaign=Badge_Grade)

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
