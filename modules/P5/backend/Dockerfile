FROM python:3.9
ENV PORT=$PORT

WORKDIR /

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY main.py /main.py
COPY vectorizer /vectorizer
COPY classifier /classifier
COPY cv /cv
COPY mlb_t /mlb_t

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
