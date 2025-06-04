FROM python:3.11

WORKDIR /app
COPY ./app /app

RUN apt-get update
RUN apt-get install vim -y

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD ["sleep", "infinity"]