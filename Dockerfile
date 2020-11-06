FROM python:3.9-buster

COPY . /mysite/
WORKDIR /mysite

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py getdb

RUN apt update && apt upgrade -y
EXPOSE 8303

ENTRYPOINT  ["./start-server.sh"]
