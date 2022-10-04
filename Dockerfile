FROM python:3.8-slim

RUN mkdir /app

COPY app/ /app/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install pipenv

COPY Pipfile /app/
COPY Pipfile.lock /app/
WORKDIR /app/

RUN pipenv lock
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
