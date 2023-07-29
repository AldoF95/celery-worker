FROM python:3.9-alpine

ENV CELERY_BROKER redis://redis:6379/0
ENV CELERY_BACKEND redis://redis:6379/1

COPY . /app
WORKDIR /app

RUN pip install -U setuptools pip
RUN pip install redis
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]