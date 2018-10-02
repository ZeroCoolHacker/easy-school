# Base image to import
FROM python:3.6-slim

# Port number to expose
EXPOSE 8000

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
