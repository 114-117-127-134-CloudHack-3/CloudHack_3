# Follow Task-0 subtask-1
FROM python:3.8-alpine
COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app
COPY ./app/ /app/
RUN apk add --update \
    && pip install --upgrade pip  \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*
CMD ["python", "app.py"]
