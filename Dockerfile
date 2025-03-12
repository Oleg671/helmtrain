FROM python:3.14.0a5-alpine3.20
WORKDIR /app
COPY codeWords.txt ./
COPY main.py ./
RUN pip install telebot | pip install pytz
CMD ['./main.py']
