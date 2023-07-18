FROM python:3.11

RUN apt update \
  && apt upgrade -y \
  && apt install -y \
  firefox-esr

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
