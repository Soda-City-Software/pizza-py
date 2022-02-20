FROM python:3.9.10-slim-buster

WORKDIR /app

COPY . /app
COPY ./pip.packages /app/pip.packages

RUN pip3 install -r pip.packages

CMD ["python3","/app/app.py"]
