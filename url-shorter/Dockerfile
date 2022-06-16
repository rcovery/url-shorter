FROM python:slim-buster

WORKDIR /home/application

COPY requirements.txt /home/application/

RUN apt update -y && apt install -y default-libmysqlclient-dev build-essential

USER application

RUN pip install -r requirements.txt

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT tail -f /dev/null