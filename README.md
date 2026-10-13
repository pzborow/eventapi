# EventAPI test project


## Description

This project shows basic usage Django,
DRF, DateTimeRangeField and Django-tenants.

It was written as a recruitment task. I gave myself a fixed amount of time for it and did as much as I could
within that time; the task brief is in `brief/`.


## Assumptions and goals

My approach for this project was to make rather
POC instead ready for use code.
The purpose for which it was created was to meet the
requirements of the task, but also for fun and learning the
multi tenant approach. I tried to keep business requirements,
but I feel free with architecture and simplification tips.

To benefit me too, I decided to use ready for use multitenant
django package, and use DateTimeRangeField instead of start
and end field to learn something new.

I'm aware of many unfinished things like missing tests, docstrings.
Also missing returning time with user timezone which was business
requirement. Mainly due to exceeding the assumed time for the 
implementation of the task.


## Folder structure

`brief` contains task brief, with task criteria. `eventapi` directory
contains all necessary files for django application,
with tests and docker's files to simplify start-up.
Application structure bases on django-tenats teneant_tutorial.
Most interesting things are located at `eventapi/events`


## Installation, start and test

Project provides docker-compose file to simplify start-up.
It provides db container and web container with postgres,
python and django.

To startup project simple execute (you should have already
installed docker and docker-compose)

    :::bash
    cd eventapi
    docker-compose up

This command start database, django application and migrate data.


## Basic usage

Tenant django app allows entering public (no tenats aware) pages via `localhost`,
it uses then `urls_public.py`, or tenant aware, then it
uses `urls_tenants.py`.

To enter tenant aware pages, you may add to your `hosts` file different
domains pointing to local server. F.e:

    :::txt
    127.0.0.1 first.test.com
    127.0.0.1 second.test.com
    # etc.

Next enter bash in docker container `docker-compose run web cli`
And inside docker call command `./manage.py create_tenant` to
add these tenants with domains. First tenant name `client_1`.

Next step should be to create user, to access API. To do so,
for `client_1` call command
`./manage.py tenant_command shell --shema=client_1`
In python shell

    :::python
    form users.factories import *
    u = UserFactory()
    # remember user name
    u.set_password('1234')
    u.save()

From now, you can use API endpoint to create data. For example
make `post` to `http://first.test.com:8000/events/` with basic auth
for above user with example data:

    :::json
    {
        "id": 1,
        "location": null,
        "owner": "use here your user's email",
        "participants": [],
        "event_name": "Beyond which around.",
        "meeting_agenda": "East through black tough.",
        "time_range": "{\"bounds\": \"[]\", \"lower\": \"2021-02-03T09:16:47.279997+00:00\", \"upper\": \"2021-02-03T11:16:47.279997+00:00\"}"
    }

You may also create some more data in shell. In the same way as above
in python shell execute:

    :::python
    from events.factories import *
    m = MeetingFactory()
    m.owner  # remember user name
    m.owner.set_password('1234')
    m.owner.save()

More data can be created similarly.


## Additional info

Additional info about django tenats cad be found here
https://django-tenants.readthedocs.io/en/latest/


## Knowing issues

At first run application can't connect to database. Application container
tires connect to database but database isn't started yet. Rerun
`docker-compose up` solve problem. 
