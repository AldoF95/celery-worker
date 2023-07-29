FROM python:3.8-slim

ENV CELERY_BROKER redis://redis:6379/0
ENV CELERY_BACKEND redis://redis:6379/1
ENV MODEL_PATH /celery/model/logReg_model

COPY . /celery
WORKDIR /celery

RUN pip install -U setuptools pip
RUN pip install redis
RUN pip install -r requirements.txt
