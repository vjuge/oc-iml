FROM python:3.9
ENV PORT=5000

WORKDIR /

COPY ./src /
COPY ./notebook/vectorizer /utils
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT main:app
