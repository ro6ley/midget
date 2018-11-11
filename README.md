[![Build Status](https://travis-ci.org/ro6ley/midget.svg?branch=master)](https://travis-ci.org/ro6ley/midget) [![Coverage Status](https://coveralls.io/repos/github/ro6ley/midget/badge.svg?branch=master)](https://coveralls.io/github/ro6ley/midget?branch=master)

# Midget

This is a url shortening application. The API receives a url and returns a shortened version
of the url, similar to [Bit.ly](http://bit.ly) and [Google URL Shortener](http://goo.gl).

The building blocks are:

* Python 3.5
* Django 2.1
* Redis

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You need the following to be able to run the project:
* Python 3 installed
* Redis
* Pipenv
* Docker (Optional)

## Setting Up for Development

These are instructions for setting up Diary API in development environment.

* check out project code:
```
  $ git clone https://github.com/ro6ley/midget.git midget_project
```

* setup the environment and install requirements:
```
  $ cd midget_project
  $ pipenv install
```

* create database tables:
```
  $ ./midget/manage.py makemigrations
  $ ./midget/manage.py migrate
```

* run development server:
```
  $ ./midget/manage.py runserver
```

The site should now be running at `http://localhost:8080/`.

To log into Django administration site as a super user,
visit `http://localhost:8080/admin`

## Documentation

Once up and running the documentation is available at: `http://localhost:8080/docs`

The endpoints in summary:

| Endpoint                 | Functionality                      |
|:------------------------ |:---------------------------------- |
| POST /api/links/         | Create a shortened URL             |
| GET /\<slug:link>        | Access the shortened URL           |
| GET /all                 | Get a list of all shortened URLs   |
| DELETE /\<slug:link>     | Delete the shortened URL           |


## Running the tests

To run the tests:

```
  $ ./midget/manage.py test --settings=settings.testing
```


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](http://www.django-rest-framework.org/) - The framework used to build the API

## Authors

* **[Robley Gori](https://github.com/ro6ley)** - *Initial work*

See also the list of [contributors](https://github.com/ro6ley/midget/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0.
