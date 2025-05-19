FROM python:latest

RUN apt-get update
RUN apt-get install -y poppler-utils

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app/ /app/app/

RUN pip install -r requirements.txt

CMD ["/bin/sh", "-c", "python -m app.main" ]