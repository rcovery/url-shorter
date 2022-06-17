FROM python:slim-buster

RUN apt update -y && apt install -y default-libmysqlclient-dev build-essential
RUN useradd -ms /bin/bash application

USER application
WORKDIR /home/application/urlsh

COPY requirements.txt /home/application/urlsh
RUN pip install -r requirements.txt

ENV PATH="${PATH}:/home/application/.local/bin"

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT tail -f /dev/null