FROM python:3.9.10-slim-buster

WORKDIR /app

COPY . /app
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python3", "/app/app.py"]
