# Kata Game

## Summary

The purpose of this project is to develop a kata game.

It contains the following files and folders:
* kata/: core code
* tests/:  unit test, integration test
* requirements.txt: all python library need
* CHANGELOG.md
* Dockerfile
* docker-compose.yml
* Makefile
* pylintrc
* README.md
* reports: this folder will be generated automatically by 'make test-unit', it gives unit test reports


## How to build and run code

* `python kata/app.py`: to run the project. You can also use docker mode with `make run`

* `make format`: to run black lib on all the code (code formatter)

* `make style`: pylint all the codes folders

* `make test`: to run both unit and integration tests

* `make test-unit`: to run unit tests

* `make test-integration`: to run integration test

* `make down: docker-compose down --volumes`: to remove declared named volumes

## Potential improvements

* Complete Unit tests, integration tests, functional tests

* May need Web Server with REST API etc

* Use redis to store kata game status if we would like to scale docker

* Add Cache if necessary, need to maintain consistency between caches and the source of truth

* Authentification for database

* Configuration should not be hardcode, could use config file or consul to store
