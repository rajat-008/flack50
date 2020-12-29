FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 80

ENV SECRET_KEY hello_world

ENTRYPOINT python3 app.py

