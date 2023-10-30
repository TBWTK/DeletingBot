FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

RUN mkdir "app"

WORKDIR "app"

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY tg_bot ./

CMD [ "python3", "./main.py"]

