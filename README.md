[![Build Status](https://travis-ci.org/ro6ley/midget.svg?branch=master)](https://travis-ci.org/ro6ley/midget) [![Coverage Status](https://coveralls.io/repos/github/ro6ley/midget/badge.svg?branch=master)](https://coveralls.io/github/ro6ley/midget?branch=master)

# Midget

This is a url shortening application. The API receives a url and returns a shortened version
of the url, similar to [Bit.ly](http://bit.ly) and [Google URL Shortener](http://goo.gl).

![Screenshot](https://user-images.githubusercontent.com/8082197/48435148-ce74d100-e78c-11e8-9bba-121f43019aec.png)


The building blocks are:

* [Django](https://www.djangoproject.com/) - The web framework used.
* [Django REST Framework](http://www.django-rest-framework.org/) - The framework used to build the API.
* [Vue JS](https://vuejs.org/) - The framework used to build the front-end application.
* [VueX](https://vuex.vuejs.org/) - The state management pattern + library for Vue.js.
* [Bootstrap + Vue](https://bootstrap-vue.js.org/) - The front-end CSS library for Vue JS.
* [Redis](https://redis.io/) - The in-memory data structure store, used as the database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You need the following installed in your machine to be able to run the project:
* Python 3.5
* Node 8+
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
  $ cd client && npm install && cd ..
```

* create database tables:
```
  $ ./midget/manage.py makemigrations
  $ ./midget/manage.py migrate
```

* start the redis server and run development server:
```
  $ redis-server /usr/local/etc/redis.conf
  $ ./midget/manage.py runserver
```

* start the client:
```
  $ cd client && npm run serve
```

The front-end should now be running at `http://localhost:8080/`.

The API will be running on `http://localhost:8000/`

## Documentation

Once up and running the API documentation is available at: `http://localhost:8000/docs`

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

## Authors

* **[Robley Gori](https://github.com/ro6ley)** - *Initial work*

See also the list of [contributors](https://github.com/ro6ley/midget/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0.
