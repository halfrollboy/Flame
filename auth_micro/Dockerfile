FROM python:3.10-alpine

WORKDIR /auth_micro
COPY ./requirements.txt /auth_micro/requirements.txt
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev bash \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip
COPY ./auth_micro /auth_micro
CMD ["uvicorn", "main2:app", "--host", "0.0.0.0", "--port", "8080"]