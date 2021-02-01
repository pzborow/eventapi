# EventAPI test project

## Description

This project show basic usage Django, DRF, DateTimeRangeField.

## Folder structure 

Brief contains task brief, with project cryteria. `eventapi` directory contains all necessary files for
django application, with tests and docker's files to simplify start-up.

## Installation and test

Project provides docker-compose file to simplify start-up. It provides postgres container and web container with
python and django.

To startup project simple execute (you should have installed docker and docker-compose)

    :::bash
    cd eventapi
    docker-compose up

This command start database, django application and migrate data.

You may also run tests

    :::bash
    docker-compose run web runtest


## Knowing issues

At first run application can't connect to database. Application container tires connect to database but database isn't started yet. Rerun
`docker-compose up` temporary solve problem.
