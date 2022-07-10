FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /home/app

RUN groupadd app && useradd app -g app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chown -R app:app $APP_HOME

USER app