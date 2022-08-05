FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .
COPY celeryworker.sh .
COPY flower.sh .


RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . .
