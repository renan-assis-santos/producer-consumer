FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONOPTIMIZE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN useradd --shell /bin/bash --create-home python
USER python

RUN mkdir /home/python/code
WORKDIR /home/python/code

COPY --chown=python . .
