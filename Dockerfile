FROM python:slim-buster

RUN apt update -y && apt install -y default-libmysqlclient-dev build-essential pkg-config
RUN useradd -ms /bin/bash application

USER application

WORKDIR /home/application/urlsh
COPY . .

RUN pip install -r requirements.txt

ENV PATH="${PATH}:/home/application/.local/bin"

ENTRYPOINT [ "sh", "entrypoint.sh" ]
