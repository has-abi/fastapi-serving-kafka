FROM tiangolo/uvicorn-gunicorn:python3.10-slim

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# COPY python dependencies
COPY ./Pipfile /usr/src/app/Pipfile
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock

# Install python dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Add app
COPY . /usr/src/app

EXPOSE 8009

CMD ["python", "main.py"]