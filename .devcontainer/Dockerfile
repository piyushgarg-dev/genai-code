FROM mcr.microsoft.com/devcontainers/python:3.12

ENV PYTHONUNBUFFERED=1


RUN sudo apt-get update && \
    sudo apt-get install -y curl

RUN apt-get install -y poppler-utils

RUN pip install --upgrade pip