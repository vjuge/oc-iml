FROM python:3.9
ENV PORT=$PORT

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE $PORT

COPY ./app-streamlit.py /app

CMD streamlit run app-streamlit.py --server.port $PORT