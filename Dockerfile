FROM python:3.8-slim

RUN mkdir /app

COPY app/ /app/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install pipenv

COPY Pipfile /app/
COPY Pipfile.lock /app/
WORKDIR /app/

RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
