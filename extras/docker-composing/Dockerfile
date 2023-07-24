# Adapted from
# https://docs.docker.com/compose/gettingstarted/

# syntax=docker/dockerfile:1
FROM python:3.10-alpine

RUN pip install --upgrade pip
RUN pip install -U pipenv

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY ["Pipfile", "Pipfile.lock", "./"] 

RUN pipenv install --system --deploy

EXPOSE 5000
COPY . .

CMD ["flask", "run"]