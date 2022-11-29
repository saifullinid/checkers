FROM python:3.10.8-slim-buster
WORKDIR /app

COPY requirements.txt ./tmp/
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install --no-cache-dir --upgrade -r ./tmp/requirements.txt

COPY . .

ENV DATABASE_HOST='db'

EXPOSE 8000

CMD ["/bin/bash", "/app/src/docker-entrypoint.sh"]