FROM python:slim-buster

RUN apt update -y && apt install -y default-libmysqlclient-dev build-essential
RUN useradd -ms /bin/bash application

USER application
WORKDIR /home/application

COPY requirements.txt /home/application/
RUN pip install -r requirements.txt

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT tail -f /dev/null