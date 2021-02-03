# EventAPI test project

## Description

This project shows basic usage Django,
DRF, DateTimeRangeField and Django-tenants.


## Assumptions and goals

This project is rather POC than ready for use code.
The purpose for which it was created was to meet the
requirements of the task, but also for fun and learning the
multitenant approach. I tried to keep business requirements,
but I feel free with architecture and simplification tips.


## Folder structure

`brief` contains task brief, with task criteria. `eventapi` directory
contains all necessary files for django application,
with tests and docker's files to simplify start-up.
Application structure bases on django-tenats teneant_tutorial.


## Installation, start and test

Project provides docker-compose file to simplify start-up.
It provides postgres container and web container with
python and django.

To startup project simple execute (you should have already
installed docker and docker-compose)

    :::bash
    cd eventapi
    docker-compose up

This command start database, django application and migrate data.

You may also run tests

    :::bash
    docker-compose run web runtest


## Basic usage

Tenant django app allows entering public (no tenats aware) pages via `localhost`,
it uses then `urls_public.py` , or tenant aware, then it
uses `urls_tenants.py`.

To enter tenant aware pages, you may add to your `hosts` file different
domains pointing to local server. F.e:

    :::txt
    127.0.0.1 first.test.com
    127.0.0.1 second.test.com

Next call command `./manage.py create_tenant` to add these two
clients with domains.

Finally, make API calls to one of two domains. You should see
separated data for every tenant.


## Knowing issues

At first run application can't connect to database. Application container
tires connect to database but database isn't started yet. Rerun
`docker-compose up` temporary solve problem.
