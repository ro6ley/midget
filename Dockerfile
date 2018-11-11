FROM python:3.7-alpine

LABEL maintainer="robleyadrian@gmail.com"

EXPOSE 8000

RUN apk --update add ${packages} && rm -rf /var/cache/apk/*

RUN pip3 install pipenv gunicorn

ADD . /midget

WORKDIR /midget

RUN pip install -r requirements.txt

RUN python midget/manage.py makemigrations

RUN python midget/manage.py migrate

CMD [ "python", "midget/manage.py", "runserver", "0.0.0.0:8000" ]
