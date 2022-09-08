FROM python:3.8

RUN mkdir -p /parsing/
WORKDIR /parsing/

COPY . /parsing/

RUN pip install pipenv
RUN pipenv install --system --deploy